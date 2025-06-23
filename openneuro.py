>>> import pandas as pd
>>> participants = pd.read_csv("C:\\Users\\Hp\\OneDrive\\derivatives\\derivatives\\participants.tsv", sep="\t")
>>> import matplotlib.pyplot as plt
>>> import seaborn as sns
>>> data = participants.sort_values("cholesterol_HDL")
>>> plt.figure(figsize=(10, 6))
<Figure size 1000x600 with 0 Axes>
>>> sns.barplot(x="participant_id", y="cholesterol_HDL", data=data, palette="coolwarm")
<stdin>:1: FutureWarning:

Passing `palette` without assigning `hue` is deprecated and will be removed in v0.14.0. Assign the `x` variable to `hue` and set `legend=False` for the same effect.

<Axes: xlabel='participant_id', ylabel='cholesterol_HDL'>
>>> plt.xticks(rotation=90)
([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191], [Text(0, 0, 'sub-76'), Text(1, 0, 'sub-67'), Text(2, 0, 'sub-51'), Text(3, 0, 'sub-33'), Text(4, 0, 'sub-78'), Text(5, 0, 'sub-29'), Text(6, 0, 'sub-66'), Text(7, 0, 'sub-01'), Text(8, 0, 'sub-17'), Text(9, 0, 'sub-47'), Text(10, 0, 'sub-41'), Text(11, 0, 'sub-50'), Text(12, 0, 'sub-57'), Text(13, 0, 'sub-71'), Text(14, 0, 'sub-23'), Text(15, 0, 'sub-32'), Text(16, 0, 'sub-24'), Text(17, 0, 'sub-28'), Text(18, 0, 'sub-08'), Text(19, 0, 'sub-52'), Text(20, 0, 'sub-03'), Text(21, 0, 'sub-10'), Text(22, 0, 'sub-30'), Text(23, 0, 'sub-38'), Text(24, 0, 'sub-22'), Text(25, 0, 'sub-02'), Text(26, 0, 'sub-35'), Text(27, 0, 'sub-19'), Text(28, 0, 'sub-75'), Text(29, 0, 'sub-63'), Text(30, 0, 'sub-77'), Text(31, 0, 'sub-14'), Text(32, 0, 'sub-72'), Text(33, 0, 'sub-21'), Text(34, 0, 'sub-36'), Text(35, 0, 'sub-11'), Text(36, 0, 'sub-61'), Text(37, 0, 'sub-13'), Text(38, 0, 'sub-45'), Text(39, 0, 'sub-06'), Text(40, 0, 'sub-74'), Text(41, 0, 'sub-55'), Text(42, 0, 'sub-62'), Text(43, 0, 'sub-44'), Text(44, 0, 'sub-60'), Text(45, 0, 'sub-26'), Text(46, 0, 'sub-16'), Text(47, 0, 'sub-37'), Text(48, 0, 'sub-12'), Text(49, 0, 'sub-15'), Text(50, 0, 'sub-80'), Text(51, 0, 'sub-65'), Text(52, 0, 'sub-40'), Text(53, 0, 'sub-05'), Text(54, 0, 'sub-46'), Text(55, 0, 'sub-18'), Text(56, 0, 'sub-39'), Text(57, 0, 'sub-64'), Text(58, 0, 'sub-49'), Text(59, 0, 'sub-27'), Text(60, 0, 'sub-31'), Text(61, 0, 'sub-59'), Text(62, 0, 'sub-73'), Text(63, 0, 'sub-70'), Text(64, 0, 'sub-42'), Text(65, 0, 'sub-43'), Text(66, 0, 'sub-07'), Text(67, 0, 'sub-48'), Text(68, 0, 'sub-34'), Text(69, 0, 'sub-04'), Text(70, 0, 'sub-54'), Text(71, 0, 'sub-25'), Text(72, 0, 'sub-58'), Text(73, 0, 'sub-09'), Text(74, 0, 'sub-56'), Text(75, 0, 'sub-20'), Text(76, 0, 'sub-100'), Text(77, 0, 'sub-101'), Text(78, 0, 'sub-102'), Text(79, 0, 'sub-104'), Text(80, 0, 'sub-105'), Text(81, 0, 'sub-106'), Text(82, 0, 'sub-107'), Text(83, 0, 'sub-108'), Text(84, 0, 'sub-109'), Text(85, 0, 'sub-110'), Text(86, 0, 'sub-112'), Text(87, 0, 'sub-113'), Text(88, 0, 'sub-114'), Text(89, 0, 'sub-115'), Text(90, 0, 'sub-116'), Text(91, 0, 'sub-117'), Text(92, 0, 'sub-118'), Text(93, 0, 'sub-119'), Text(94, 0, 'sub-120'), Text(95, 0, 'sub-121'), Text(96, 0, 'sub-122'), Text(97, 0, 'sub-123'), Text(98, 0, 'sub-124'), Text(99, 0, 'sub-125'), Text(100, 0, 'sub-126'), Text(101, 0, 'sub-127'), Text(102, 0, 'sub-128'), Text(103, 0, 'sub-129'), Text(104, 0, 'sub-130'), Text(105, 0, 'sub-131'), Text(106, 0, 'sub-132'), Text(107, 0, 'sub-133'), Text(108, 0, 'sub-134'), Text(109, 0, 'sub-135'), Text(110, 0, 'sub-136'), Text(111, 0, 'sub-137'), Text(112, 0, 'sub-138'), Text(113, 0, 'sub-140'), Text(114, 0, 'sub-141'), Text(115, 0, 'sub-142'), Text(116, 0, 'sub-143'), Text(117, 0, 'sub-144'), Text(118, 0, 'sub-145'), Text(119, 0, 'sub-146'), Text(120, 0, 'sub-147'), Text(121, 0, 'sub-148'), Text(122, 0, 'sub-149'), Text(123, 0, 'sub-150'), Text(124, 0, 'sub-151'), Text(125, 0, 'sub-152'), Text(126, 0, 'sub-153'), Text(127, 0, 'sub-155'), Text(128, 0, 'sub-156'), Text(129, 0, 'sub-159'), Text(130, 0, 'sub-160'), Text(131, 0, 'sub-161'), Text(132, 0, 'sub-162'), Text(133, 0, 'sub-163'), Text(134, 0, 'sub-164'), Text(135, 0, 'sub-165'), Text(136, 0, 'sub-166'), Text(137, 0, 'sub-167'), Text(138, 0, 'sub-168'), Text(139, 0, 'sub-169'), Text(140, 0, 'sub-171'), Text(141, 0, 'sub-172'), Text(142, 0, 'sub-173'), Text(143, 0, 'sub-174'), Text(144, 0, 'sub-175'), Text(145, 0, 'sub-176'), Text(146, 0, 'sub-177'), Text(147, 0, 'sub-178'), Text(148, 0, 'sub-179'), Text(149, 0, 'sub-180'), Text(150, 0, 'sub-181'), Text(151, 0, 'sub-182'), Text(152, 0, 'sub-183'), Text(153, 0, 'sub-184'), Text(154, 0, 'sub-185'), Text(155, 0, 'sub-186'), Text(156, 0, 'sub-187'), Text(157, 0, 'sub-188'), Text(158, 0, 'sub-189'), Text(159, 0, 'sub-190'), Text(160, 0, 'sub-191'), Text(161, 0, 'sub-192'), Text(162, 0, 'sub-193'), Text(163, 0, 'sub-194'), Text(164, 0, 'sub-195'), Text(165, 0, 'sub-196'), Text(166, 0, 'sub-197'), Text(167, 0, 'sub-198'), Text(168, 0, 'sub-199'), Text(169, 0, 'sub-200'), Text(170, 0, 'sub-53'), Text(171, 0, 'sub-68'), Text(172, 0, 'sub-79'), Text(173, 0, 'sub-81'), Text(174, 0, 'sub-82'), Text(175, 0, 'sub-83'), Text(176, 0, 'sub-84'), Text(177, 0, 'sub-85'), Text(178, 0, 'sub-86'), Text(179, 0, 'sub-87'), Text(180, 0, 'sub-88'), Text(181, 0, 'sub-89'), Text(182, 0, 'sub-90'), Text(183, 0, 'sub-91'), Text(184, 0, 'sub-92'), Text(185, 0, 'sub-93'), Text(186, 0, 'sub-94'), Text(187, 0, 'sub-95'), Text(188, 0, 'sub-96'), Text(189, 0, 'sub-97'), Text(190, 0, 'sub-98'), Text(191, 0, 'sub-99')])
>>> plt.title("HDL Cholesterol Levels by Participant")
Text(0.5, 1.0, 'HDL Cholesterol Levels by Participant')
>>> plt.ylabel("HDL (mg/dL)")
Text(0, 0.5, 'HDL (mg/dL)')
>>> plt.xlabel("Participant")
Text(0.5, 0, 'Participant')
>>> plt.tight_layout()
>>> plt.show()
<stdin>:1: UserWarning: FigureCanvasAgg is non-interactive, and thus cannot be shown
>>> plt.savefig("cholesterol_plot.png", dpi=300)
>>> print("Plot saved as cholesterol_plot.png")
Plot saved as cholesterol_plot.png
>>> import os
>>> os.startfile("cholesterol_plot.png")
>>> plt.title("HDL Cholesterol Levels by Participant")
Text(0.5, 1.0, 'HDL Cholesterol Levels by Participant')
>>> plt.ylabel("HDL (mg/dL)")
Text(0, 0.5, 'HDL (mg/dL)')
>>> plt.xlabel("Participant")
Text(0.5, 0, 'Participant')
>>> plt.tight_layout()
>>> plt.show()
<stdin>:1: UserWarning: FigureCanvasAgg is non-interactive, and thus cannot be shown
>>> plt.savefig("cholesterol_plot.png", dpi=300)
>>> print("Plot saved as cholesterol_plot.png")
Plot saved as cholesterol_plot.png
>>>  open cholesterol_plot.png
  File "<stdin>", line 1
    open cholesterol_plot.png
IndentationError: unexpected indent
>>> import os
>>> os.startfile("cholesterol_plot.png")
>>> plt.figure(figsize=(8, 5))
<Figure size 800x500 with 0 Axes>
>>> sns.histplot(participants["hemoglobin"], bins=15, kde=True, color='skyblue')
<Axes: xlabel='hemoglobin', ylabel='Count'>
>>> plt.title("Distribution of Hemoglobin")
Text(0.5, 1.0, 'Distribution of Hemoglobin')
>>> plt.xlabel("Hemoglobin (g/dL)")
Text(0.5, 0, 'Hemoglobin (g/dL)')
>>> plt.ylabel("Count")
Text(0, 0.5, 'Count')
>>> plt.show()
<stdin>:1: UserWarning: FigureCanvasAgg is non-interactive, and thus cannot be shown
>>> plt.savefig("hemoglobin_plot.png", dpi=300)
>>> print("Plot saved as hemoglobin_plot.png")
Plot saved as hemoglobin_plot.png
>>> os.startfile("hemoglobin_plot.png")
>>> plt.figure(figsize=(7, 5))
<Figure size 700x500 with 0 Axes>
>>> sns.scatterplot(data=participants, x="cholesterol_HDL", y="LDL_cholesterol", hue="sex", style="sex")
<Axes: xlabel='cholesterol_HDL', ylabel='LDL_cholesterol'>
>>> plt.title("HDL vs LDL Cholesterol")
Text(0.5, 1.0, 'HDL vs LDL Cholesterol')
>>> plt.xlabel("HDL (mg/dL)")
Text(0.5, 0, 'HDL (mg/dL)')
>>> plt.ylabel("LDL (mg/dL)")
Text(0, 0.5, 'LDL (mg/dL)')
>>> plt.grid(True)
>>> plt.show()
<stdin>:1: UserWarning: FigureCanvasAgg is non-interactive, and thus cannot be shown
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

[5 rows x 13 columns]
>>> for col in ['APOE_rs429358', 'APOE_rs7412', 'PICALM_rs3851179', 'sex']:
...   df[col] = pd.Categorical(df[col]).codes
...
<stdin>:2: SettingWithCopyWarning:
A value is trying to be set on a copy of a slice from a DataFrame.
Try using .loc[row_indexer,col_indexer] = value instead

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
<stdin>:2: SettingWithCopyWarning:
A value is trying to be set on a copy of a slice from a DataFrame.
Try using .loc[row_indexer,col_indexer] = value instead

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
<stdin>:2: SettingWithCopyWarning:
A value is trying to be set on a copy of a slice from a DataFrame.
Try using .loc[row_indexer,col_indexer] = value instead

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
>>> df = participants[available_columns].copy()
>>> for col in ['APOE_rs429358', 'APOE_rs7412', 'PICALM_rs3851179', 'sex']:
...     df[col] = pd.Categorical(df[col]).codes
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

[13 rows x 13 columns]
>>> correlation_matrix.to_csv("correlations.csv")
>>> os.startfile("correlations.csv")
>>> import seaborn as sns
>>> import matplotlib.pyplot as plt
>>> plt.figure(figsize=(10, 8))
<Figure size 1000x800 with 0 Axes>
>>> sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f")
<Axes: >
>>> plt.title("Correlation Matrix: APOE, PICALM & Other Variables")
Text(0.5, 1.0, 'Correlation Matrix: APOE, PICALM & Other Variables')
>>> plt.tight_layout()
>>> plt.savefig("correlation_heatmap.png")
>>> os.startfile("correlation_heatmap.png")
