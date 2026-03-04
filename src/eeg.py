>>> import mne
>>> raw = mne.io.read_raw_eeglab(r"C:\Users\Hp\OneDrive\derivatives\eeglab\derivatives\eeglab\sub-001\eeg\sub-001_task-photomark_eeg.set", preload=True)
>>> raw.plot()
>>> epochs = mne.Epochs(raw, events, event_id, tmin=-0.2, tmax=0.8, baseline=(None, 0), preload=True)
>>> epochs.plot()
>>> from numpy import std
>>> flat_channels = [
...     ch for ch in raw.info['ch_names']
...     if std(raw.copy().pick_channels([ch]).get_data()) < 1e-6
... ]
>>>>>> import numpy as np
>>> threshold = 5e-5
>>> noisy_channels = [
...     ch for ch in raw.info['ch_names']
...     if np.std(raw.copy().pick(picks=[ch]).get_data()) > threshold
... ]
>>> print("Noisy channels:", noisy_channels)
>>> raw.filter(1., 40., fir_design='firwin')
>>> ica = mne.preprocessing.ICA(n_components=19, random_state=97)
>>> ica.fit(raw)
>>> ica.plot_components()
>>> ica.plot_sources(raw, picks=[5, 8, 17])
>>> ica.exclude.append(8)
>>> ica.plot_components(picks=[8, 17])

Spectrogram (Power Spectral Density)
For raw continuous data:
>>> raw.plot_psd(fmin=1., fmax=50.)
for epoched data
>>> epochs.plot_psd(fmin=1., fmax=50.)
Time-Frequency Spectrogram of Epochs
>>> from mne.time_frequency import tfr_multitaper
>>> power = tfr_multitaper(epochs, freqs=np.arange(4, 40, 2), n_cycles=4, return_itc=False)
>>> power.plot(picks='Pz', baseline=(None, 0), mode='logratio')

>>> ica.exclude.extend([3, 4, 8])
>>> raw_clean = ica.apply(raw.copy())
>>> save_path = "cleaned_fp1_fp2_raw.fif"
>>> raw_clean.save(save_path, overwrite=True)
>>> import numpy as np
>>> import matplotlib.pyplot as plt
>>> channels = ['Fp1', 'Fp2']
>>> freqs = np.linspace(2, 40, 20)
>>> n_cycles = freqs / 2.
>>> raw_before_path = r"C:\Users\Hp\OneDrive\derivatives\eeglab\derivatives\eeglab\sub-001\eeg\sub-001_task-photomark_eeg.set"
>>> raw_after_path = r"C:\Users\Hp\cleaned_fp1_fp2_raw.fif"
>>> raw_before = mne.io.read_raw_eeglab(raw_before_path, preload=True)
>>> picks = mne.pick_channels(raw_before.info['ch_names'], include=channels)
>>> events_before = mne.make_fixed_length_events(raw_before, duration=1.0)
>>> events_after = mne.make_fixed_length_events(raw_after, duration=1.0)
>>> epochs_before = mne.Epochs(raw_before, events_before, tmin=0, tmax=1.0, picks=picks,
...                            baseline=None, preload=True)
>>> power_before = mne.time_frequency.tfr_multitaper(epochs_before, freqs=freqs,
...                                                  n_cycles=n_cycles, return_itc=False)
>>> power_before.plot([0], title='Fp1 Before ICA', baseline=(0, 0.5), mode='logratio')
>>> power_before.plot([1], title='Fp2 Before ICA', baseline=(0, 0.5), mode='logratio')power_before.plot([1], title='Fp2 Before ICA', 
>>>  power_before.plot([1], title='Fp2 Before ICA', baseline=(0, 0.5), mode='logratio')power_before.plot([1], title='Fp2 Before ICA', baseline=(0, 0.5), mode='logratio')                                                                                                    


