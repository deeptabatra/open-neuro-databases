import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import yaml

with open("config/params.yaml") as f:
    config = yaml.safe_load(f)

input_path = config["paths"]["biomarker_input"]
results_dir = config["paths"]["results_dir"]
figures_dir = os.path.join(results_dir, "figures")
os.makedirs(figures_dir, exist_ok=True)

genetic_markers = config["biomarker_analysis"]["genetic_markers"]
demographic_cols = config["biomarker_analysis"]["demographic_columns"]
blood_markers = config["biomarker_analysis"]["blood_markers"]
cognitive_cols = config["biomarker_analysis"]["cognitive_columns"]
corr_method = config["biomarker_analysis"]["correlation_method"]

# --- Load data ---
participants = pd.read_csv(input_path, sep="\t")

# --- HDL Cholesterol by participant ---
data = participants.sort_values("cholesterol_HDL")
plt.figure(figsize=(10, 6))
sns.barplot(x="participant_id", y="cholesterol_HDL", data=data, palette="coolwarm")
plt.title("HDL Cholesterol Levels by Participant")
plt.ylabel("HDL (mg/dL)")
plt.xlabel("Participant")
plt.tight_layout()
plt.savefig(os.path.join(figures_dir, "cholesterol_plot.png"), dpi=300)
print("Plot saved: cholesterol_plot.png")
plt.close()

# --- Hemoglobin distribution ---
plt.figure(figsize=(8, 5))
sns.histplot(participants["hemoglobin"], bins=15, kde=True, color='skyblue')
plt.title("Distribution of Hemoglobin")
plt.xlabel("Hemoglobin (g/dL)")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig(os.path.join(figures_dir, "hemoglobin_plot.png"), dpi=300)
print("Plot saved: hemoglobin_plot.png")
plt.close()

# --- HDL vs LDL scatter ---
plt.figure(figsize=(7, 5))
sns.scatterplot(data=participants, x="cholesterol_HDL", y="LDL_cholesterol",
                hue="sex", style="sex")
plt.title("HDL vs LDL Cholesterol")
plt.xlabel("HDL (mg/dL)")
plt.ylabel("LDL (mg/dL)")
plt.grid(True)
plt.tight_layout()
plt.savefig(os.path.join(figures_dir, "hdlvsldlplot.png"), dpi=300)
print("Plot saved: hdlvsldlplot.png")
plt.close()

# --- Correlation analysis ---
columns_of_interest = genetic_markers + demographic_cols + blood_markers + cognitive_cols
available_columns = [col for col in columns_of_interest if col in participants.columns]
df = participants[available_columns].copy()

for col in genetic_markers + ["sex"]:
    if col in df.columns:
        df[col] = pd.Categorical(df[col]).codes

df_clean = df.dropna()
correlation_matrix = df_clean.corr(method=corr_method)
print(correlation_matrix)

correlation_matrix.to_csv(os.path.join(results_dir, "correlations.csv"))
print("Correlation matrix saved: correlations.csv")

# --- Correlation heatmap ---
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Matrix: APOE, PICALM & Other Variables")
plt.tight_layout()
plt.savefig(os.path.join(figures_dir, "correlation_heatmap.png"), dpi=300)
print("Plot saved: correlation_heatmap.png")
plt.close()
