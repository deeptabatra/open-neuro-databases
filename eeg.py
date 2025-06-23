C:\Users\Hp> C:\Users\Hp\AppData\Local\Programs\Python\Python311\python.exe
Python 3.11.0 (main, Oct 24 2022, 18:26:48) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import mne
>>> raw = mne.io.read_raw_eeglab(r"C:\Users\Hp\OneDrive\derivatives\eeglab\derivatives\eeglab\sub-001\eeg\sub-001_task-photomark_eeg.set", preload=True)
<stdin>:1: RuntimeWarning: The data contains 'boundary' events, indicating data discontinuities. Be cautious of filtering and epoching around these events.
>>> raw.plot()
Using matplotlib as 2D backend.
<MNEBrowseFigure size 800x800 with 4 Axes>
>>> Channels marked as bad:
none
events, event_id = mne.events_from_annotations(raw)
Used Annotations descriptions: [np.str_('\x1a\x1a\x1a\x1a\x1a          '), np.str_('CAL mode'), np.str_('PAT 2 \x1a\x1a\x1a\x1a CAL  '), np.str_('PHOTO 20Hz          '), np.str_('PHOTO 5Hz           '), np.str_('Photo/HV mark'), np.str_('RESET condition'), np.str_('Y\x1a\x1a\x1a\x1a\x1a\x1a       '), np.str_('boundary'), np.str_('closed eyes'), np.str_('eye movement'), np.str_('open eyes')]
>>> epochs = mne.Epochs(raw, events, event_id, tmin=-0.2, tmax=0.8, baseline=(None, 0), preload=True)
Not setting metadata
538 matching events found
Setting baseline interval to [-0.2, 0.0] s
Applying baseline correction (mode: mean)
0 projection items activated
Using data from preloaded Raw for 538 events and 501 original time points ...
0 bad epochs dropped
>>> epochs.plot()
<MNEBrowseFigure size 800x800 with 4 Axes>
>>> Dropped 0 epochs:
The following epochs were marked as bad and are dropped:
[]
Channels marked as bad:
none

>>> from numpy import std
>>> flat_channels = [
...     ch for ch in raw.info['ch_names']
...     if std(raw.copy().pick_channels([ch]).get_data()) < 1e-6
... ]
NOTE: pick_channels() is a legacy function. New code should use inst.pick(...).
NOTE: pick_channels() is a legacy function. New code should use inst.pick(...).
NOTE: pick_channels() is a legacy function. New code should use inst.pick(...).
NOTE: pick_channels() is a legacy function. New code should use inst.pick(...).
NOTE: pick_channels() is a legacy function. New code should use inst.pick(...).
NOTE: pick_channels() is a legacy function. New code should use inst.pick(...).
NOTE: pick_channels() is a legacy function. New code should use inst.pick(...).
NOTE: pick_channels() is a legacy function. New code should use inst.pick(...).
NOTE: pick_channels() is a legacy function. New code should use inst.pick(...).
NOTE: pick_channels() is a legacy function. New code should use inst.pick(...).
NOTE: pick_channels() is a legacy function. New code should use inst.pick(...).
NOTE: pick_channels() is a legacy function. New code should use inst.pick(...).
NOTE: pick_channels() is a legacy function. New code should use inst.pick(...).
NOTE: pick_channels() is a legacy function. New code should use inst.pick(...).
NOTE: pick_channels() is a legacy function. New code should use inst.pick(...).
NOTE: pick_channels() is a legacy function. New code should use inst.pick(...).
NOTE: pick_channels() is a legacy function. New code should use inst.pick(...).
NOTE: pick_channels() is a legacy function. New code should use inst.pick(...).
NOTE: pick_channels() is a legacy function. New code should use inst.pick(...).
>>> print("Flat channels:", flat_channels)
Flat channels: []
>>>>>> import numpy as np
>>> threshold = 5e-5
>>> noisy_channels = [
...     ch for ch in raw.info['ch_names']
...     if np.std(raw.copy().pick(picks=[ch]).get_data()) > threshold
... ]
>>> print("Noisy channels:", noisy_channels)
Noisy channels: []
>>> raw.filter(1., 40., fir_design='firwin')
Filtering raw data in 1 contiguous segment
Setting up band-pass filter from 1 - 40 Hz

FIR filter parameters
---------------------
Designing a one-pass, zero-phase, non-causal bandpass filter:
- Windowed time-domain design (firwin) method
- Hamming window with 0.0194 passband ripple and 53 dB stopband attenuation
- Lower passband edge: 1.00
- Lower transition bandwidth: 1.00 Hz (-6 dB cutoff frequency: 0.50 Hz)
- Upper passband edge: 40.00 Hz
- Upper transition bandwidth: 10.00 Hz (-6 dB cutoff frequency: 45.00 Hz)
- Filter length: 1651 samples (3.302 s)

<RawEEGLAB | sub-001_task-photomark_eeg.set, 19 x 151675 (303.4 s), ~22.0 MiB, data loaded>
>>> ica = mne.preprocessing.ICA(n_components=20, random_state=97)
>>> ica.fit(raw)
>>> raw.filter(1., 40., fir_design='firwin')
Filtering raw data in 1 contiguous segment
Setting up band-pass filter from 1 - 40 Hz

FIR filter parameters
---------------------
Designing a one-pass, zero-phase, non-causal bandpass filter:
- Windowed time-domain design (firwin) method
- Hamming window with 0.0194 passband ripple and 53 dB stopband attenuation
- Lower passband edge: 1.00
- Lower transition bandwidth: 1.00 Hz (-6 dB cutoff frequency: 0.50 Hz)
- Upper passband edge: 40.00 Hz
- Upper transition bandwidth: 10.00 Hz (-6 dB cutoff frequency: 45.00 Hz)
- Filter length: 1651 samples (3.302 s)

<RawEEGLAB | sub-001_task-photomark_eeg.set, 19 x 151675 (303.4 s), ~22.0 MiB, data loaded>
>>> ica = mne.preprocessing.ICA(n_components=20, random_state=97)
>>> ica.fit(raw)
>>> install sklearn package
  Fitting ICA to data using 19 channels (please be patient, this may take a while)
T>>> ica = mne.preprocessing.ICA(n_components=19, random_state=97)
>>> ica.fit(raw)
Fitting ICA to data using 19 channels (please be patient, this may take a while)
Selecting by number: 19 components
<stdin>:1: RuntimeWarning: Using n_components=19 (resulting in n_components_=19) may lead to an unstable mixing matrix estimation because the ratio between the largest (17) and smallest (3.3e-15) variances is too large (> 1e6); consider setting n_components=0.999999 or an integer <= 17
Fitting ICA took 31.6s.
<ICA | raw data decomposition, method: fastica (fit in 68 iterations on 151675 samples), 19 ICA components (19 PCA components available), channel types: eeg, no sources marked for exclusion>
>>> ica.plot_components()
<MNEFigure size 1920x974 with 19 Axes>
>>>
>>>
>>> ica.plot_sources(raw, picks=[5, 8, 17])
Creating RawArray with float64 data, n_channels=3, n_times=151675
    Range : 0 ... 151674 =      0.000 ...   303.348 secs
Ready.
<MNEBrowseFigure size 800x800 with 4 Axes>
>>>
>>>
>>>
>>>
>>> ica.plot_sources(raw, picks=[5, 8, 17])
Creating RawArray with float64 data, n_channels=3, n_times=151675
    Range : 0 ... 151674 =      0.000 ...   303.348 secs
Ready.
<MNEBrowseFigure size 800x800 with 4 Axes>
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


