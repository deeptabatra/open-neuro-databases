import numpy as np
import matplotlib.pyplot as plt
import mne
from mne.time_frequency import tfr_multitaper
import yaml

with open("config/params.yaml") as f:
    config = yaml.safe_load(f)

raw_path = config["paths"]["eeg_input"]
cleaned_path = config["paths"]["eeg_cleaned_output"]
bp_low = config["eeg_preprocessing"]["bandpass_low"]
bp_high = config["eeg_preprocessing"]["bandpass_high"]
n_components = config["eeg_preprocessing"]["ica_n_components"]
random_state = config["eeg_preprocessing"]["ica_random_state"]
noisy_threshold = config["eeg_preprocessing"]["noisy_channel_threshold"]
flat_threshold = config["eeg_preprocessing"]["flat_channel_threshold"]
channels = config["eeg_preprocessing"]["channels_of_interest"]

# --- Load raw EEG ---
raw = mne.io.read_raw_eeglab(raw_path, preload=True)
raw.plot()

# --- Detect flat and noisy channels ---
flat_channels = [
    ch for ch in raw.info['ch_names']
    if np.std(raw.copy().pick_channels([ch]).get_data()) < flat_threshold
]
noisy_channels = [
    ch for ch in raw.info['ch_names']
    if np.std(raw.copy().pick(picks=[ch]).get_data()) > noisy_threshold
]
print("Flat channels:", flat_channels)
print("Noisy channels:", noisy_channels)

# --- Bandpass filter ---
raw.filter(bp_low, bp_high, fir_design='firwin')

# --- ICA ---
ica = mne.preprocessing.ICA(n_components=n_components, random_state=random_state)
ica.fit(raw)
ica.plot_components()
ica.plot_sources(raw, picks=[5, 8, 17])
ica.exclude.extend([3, 4, 8])

# --- Apply ICA and save cleaned data ---
raw_clean = ica.apply(raw.copy())
raw_clean.save(cleaned_path, overwrite=True)
print(f"Cleaned data saved to: {cleaned_path}")

# --- Power Spectral Density ---
raw.compute_psd(fmin=bp_low, fmax=50.).plot()

# --- Time-frequency analysis on Fp1/Fp2 before and after ICA ---
raw_after = mne.io.read_raw_fif(cleaned_path, preload=True)
freqs = np.linspace(2, 40, 20)
n_cycles = freqs / 2.

for raw_obj, label in [(raw, "Before ICA"), (raw_after, "After ICA")]:
    picks = mne.pick_channels(raw_obj.info['ch_names'], include=channels)
    events = mne.make_fixed_length_events(raw_obj, duration=1.0)
    epochs = mne.Epochs(raw_obj, events, tmin=0, tmax=1.0, picks=picks,
                        baseline=None, preload=True)
    power = tfr_multitaper(epochs, freqs=freqs, n_cycles=n_cycles, return_itc=False)
    power.plot([0], title=f'Fp1 {label}', baseline=(0, 0.5), mode='logratio')
    power.plot([1], title=f'Fp2 {label}', baseline=(0, 0.5), mode='logratio')
