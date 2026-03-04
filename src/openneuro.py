>>> import pandas as pd
>>> participants = pd.read_csv("C:\\Users\\Hp\\OneDrive\\derivatives\\derivatives\\participants.tsv", sep="\t")
>>> import matplotlib.pyplot as plt
>>> import seaborn as sns
>>> data = participants.sort_values("cholesterol_HDL")
>>> plt.figure(figsize=(10, 6))
>>> sns.barplot(x="participant_id", y="cholesterol_HDL", data=data, palette="coolwarm")
>>> plt.ylabel("HDL (mg/dL)")
>>> plt.xlabel("Participant")
>>> plt.tight_layout()
>>> plt.show()
>>> plt.savefig("cholesterol_plot.png", dpi=300)
>>> print("Plot saved as cholesterol_plot.png")
Plot saved as cholesterol_plot.png
>>> import os
>>> os.startfile("cholesterol_plot.png")
>>> plt.title("HDL Cholesterol Levels by Participant")
>>> plt.ylabel("HDL (mg/dL)")
>>> plt.xlabel("Participant")
>>> plt.tight_layout()
>>> plt.show()
>>> plt.savefig("cholesterol_plot.png", dpi=300)
>>> print("Plot saved as cholesterol_plot.png")
  >>> import os
>>> os.startfile("cholesterol_plot.png")
>>> plt.figure(figsize=(8, 5))
<Figure size 800x500 with 0 Axes>
>>> sns.histplot(participants["hemoglobin"], bins=15, kde=True, color='skyblue')
<Axes: xlabel='hemoglobin', ylabel='Count'>
>>> plt.title("Distribution of Hemoglobin")
>>> plt.xlabel("Hemoglobin (g/dL)")
>>> plt.ylabel("Count")
>>> plt.show()
>>> plt.savefig("hemoglobin_plot.png", dpi=300)
>>> print("Plot saved as hemoglobin_plot.png")
Plot saved as hemoglobin_plot.png
>>> os.startfile("hemoglobin_plot.png")
>>> plt.figure(figsize=(7, 5))
>>> sns.scatterplot(data=participants, x="cholesterol_HDL", y="LDL_cholesterol", hue="sex", style="sex")
>>> plt.title("HDL vs LDL Cholesterol")
>>> plt.xlabel("HDL (mg/dL)")
>>> plt.ylabel("LDL (mg/dL)")
>>> plt.grid(True)
>>> plt.show()
>>> plt.savefig("hdlvsldlplot.png", dpi=300)
>>> print("Plot saved as hdlvsldlplot.png")
Plot saved as hdlvsldlplot.png
>>> os.startfile("hdlvsldlplot.png")
>>> columns_of_interest = [
...     'APOE_rs429358', 'APOE_rs7412', 'PICALM_rs3851179',  # genetic markers
...     'age', 'sex',                                        # demographics
...     'cholesterol_HDL', 'LDL_cholesterol', 'triglycerides',  # blood markers
...     'CVLT_3', 'CVLT_4', 'MINI-COPE_5', 'BDI', 'RPM'         # cognitive/performance
... ]
>>> available_columns = [col for col in columns_of_interest if col in participants.columns]
>>> df = participants[available_columns]
>>> print(df.head())
  APOE_rs429358 APOE_rs7412 PICALM_rs3851179  age  sex  cholesterol_HDL  ...  triglycerides  CVLT_3  CVLT_4  MINI-COPE_5  BDI  RPM
0           T/T         C/C              A/A   59    0             37.9  ...          179.6      16      10          1.0   16   50
1           T/T         C/C              G/A   56    0             46.1  ...          163.7      15       6          0.5    8   56
2           T/T         C/C              G/A   52    0             43.3  ...           43.6       9       6          1.5   11   52
3           T/T         C/C              A/A   52    1             83.2  ...           81.5      16       8          0.0   20   58
4           T/T         C/C              G/A   52    1             66.1  ...          143.6      15       7          1.0    2   53

>>> for col in ['APOE_rs429358', 'APOE_rs7412', 'PICALM_rs3851179', 'sex']:
...   df[col] = pd.Categorical(df[col]).codes
...
>>> df_clean = df.dropna()
>>> correlation_matrix = df_clean.corr(method='pearson')
>>> print(correlation_matrix)
                  APOE_rs429358  APOE_rs7412  PICALM_rs3851179       age  ...    CVLT_4  MINI-COPE_5       BDI       RPM
APOE_rs429358          1.000000    -0.057275         -0.501482 -0.147369  ... -0.048046    -0.110267 -0.066640  0.108749
APOE_rs7412           -0.057275     1.000000          0.169323  0.134183  ...  0.050920     0.004853 -0.028602 -0.121284
PICALM_rs3851179      -0.501482     0.169323          1.000000  0.124345  ...  0.024844     0.126596 -0.011797 -0.063344
age                   -0.147369     0.134183          0.124345  1.000000  ...  0.076034     0.058653 -0.089477 -0.231492
sex                    0.008054     0.113919          0.051922 -0.068543  ...  0.184470    -0.226994 -0.071649 -0.065978
cholesterol_HDL        0.159132     0.067765          0.113669 -0.031995  ...  0.100419    -0.415738  0.055812 -0.011551
LDL_cholesterol        0.088196     0.050290          0.037288  0.008498  ... -0.021725    -0.080931  0.111935 -0.164331
triglycerides         -0.136727     0.023651         -0.068417 -0.041379  ... -0.202259     0.167475  0.118518 -0.085167
CVLT_3                -0.063817     0.123207         -0.026954 -0.089648  ...  0.282616    -0.253794 -0.127930  0.204657
CVLT_4                -0.048046     0.050920          0.024844  0.076034  ...  1.000000    -0.139865 -0.066684  0.206197
MINI-COPE_5           -0.110267     0.004853          0.126596  0.058653  ... -0.139865     1.000000 -0.036298 -0.086895
BDI                   -0.066640    -0.028602         -0.011797 -0.089477  ... -0.066684    -0.036298  1.000000 -0.139913
RPM                    0.108749    -0.121284         -0.063344 -0.231492  ...  0.206197    -0.086895 -0.139913  1.000000

>>> correlation_matrix.to_csv("correlations.csv")
>>> os.startfile("correlations.csv")
>>> import seaborn as sns
>>> import matplotlib.pyplot as plt
>>> plt.figure(figsize=(10, 8))
>>> sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f")
>>> plt.title("Correlation Matrix: APOE, PICALM & Other Variables")
>>> plt.tight_layout()
>>> plt.savefig("correlation_heatmap.png")
>>> os.startfile("correlation_heatmap.png")
