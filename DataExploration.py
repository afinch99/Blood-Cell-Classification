import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# read in the data
path = "/Users/tylerrowe/Desktop/College/24Fall/Applied ML/AML-ClassifyingBloodImages/images"
df = pd.read_csv(f"{path}/bounding_box_annotations.csv")

# show distribution of labels and save the plot
plt.figure(figsize=(10, 6))
sns.countplot(x="label", data=df)
plt.title("Cell Type Distribution")
plt.xlabel("Cell Type")
plt.ylabel("Count")
plt.savefig(f"{path}/Distribution_of_Cells.png")

