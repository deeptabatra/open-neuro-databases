# OpenNeuro Datasets Analysis

Python scripts for analysing publicly available neuroscience datasets from [OpenNeuro](https://openneuro.org).
Covers EEG preprocessing and blood biomarker correlation analysis.

---

## Repository Structure

```
open-neuro-databases/
├── config/
│   └── params.yaml              # dataset paths, preprocessing parameters, column names
├── data/
│   ├── raw/                     # downloaded dataset files (not tracked by git)
│   └── processed/               # cleaned outputs
├── src/
│   ├── eeg.py                   # EEG preprocessing & visualisation
│   └── openneuro.py             # blood biomarker correlation analysis
├── results/
│   └── figures/                 # output plots
├── requirements.txt
└── README.md
```

---

## Analyses

### 1. EEG Preprocessing (`src/eeg.py`)

**Dataset:** [ds006036 v1.0.5](https://openneuro.org/datasets/ds006036/versions/1.0.5)

| Step | Description |
|------|-------------|
| Load | Read raw EEG from EEGLAB `.set` format via MNE |
| Filter | Bandpass filter 1–40 Hz |
| Artefact detection | Flag noisy and flat channels by standard deviation thresholds |
| ICA | Independent Component Analysis (19 components) for artefact correction |
| Epochs | Segment data around events (−0.2 to 0.8 s) |
| Visualisation | Raw signals, ICA components, power spectral density, time-frequency spectrograms |

### 2. Blood Biomarker Analysis (`src/openneuro.py`)

**Dataset:** [ds004796 v1.0.9](https://openneuro.org/datasets/ds004796/versions/1.0.9)

Investigates correlations between genetic variants and other factors:

| Variable group | Columns |
|---|---|
| Genetic markers | APOE (rs429358, rs7412), PICALM (rs3851179) |
| Demographics | age, sex |
| Blood markers | HDL cholesterol, LDL cholesterol, triglycerides |
| Cognitive scores | CVLT-3, CVLT-4, MINI-COPE, BDI, RPM |

Outputs Pearson correlation matrix and heatmap visualisation.

---

## Usage

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Download datasets
Download datasets from OpenNeuro and place them in `data/raw/`. Update file paths in `config/params.yaml`.

### 3. Run scripts
```bash
python src/eeg.py
python src/openneuro.py
```

---

## Dependencies

| Package | Purpose |
|---------|---------|
| `mne` | EEG data loading, preprocessing, ICA |
| `pandas` | Tabular data handling |
| `numpy` | Numerical operations |
| `matplotlib` | Plotting |
| `seaborn` | Statistical visualisation |
