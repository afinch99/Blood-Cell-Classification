import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Read in labels from labels.csv
path = '/Users/tylerrowe/Desktop/College/24Fall/Applied ML/AML-ClassifyingBloodImages/Data/'
image_labels = pd.read_csv(path + 'dataset-master/labels.csv')

# Create a new column to check if an image contains more than one type of WBC
image_labels['Multiple_WBC'] = image_labels['Category'].str.contains(',')

# Map the 'Category' column to your desired categories
category_map = {
    'EOSINOPHIL': 'EOSINOPHIL',
    'LYMPHOCYTE': 'LYMPHOCYTE',
    'MONOCYTE': 'MONOCYTE',
    'NEUTROPHIL': 'NEUTROPHIL'
}

# Apply the mapping to create a new 'Mapped_Category' column
image_labels['Mapped_Category'] = image_labels['Category'].str.split(',').str[0].map(category_map)

# Visualize the distribution of labels
plt.figure(figsize=(10, 6))
sns.countplot(data=image_labels, x='Mapped_Category', hue='Multiple_WBC')
plt.title('Distribution of White Blood Cells')
plt.xlabel('White Blood Cell Type')
plt.ylabel('Count')

# Set custom x-axis labels
plt.xticks(rotation=0)
plt.xticks(ticks=range(4), labels=['EOSINOPHIL', 'LYMPHOCYTE', 'MONOCYTE', 'NEUTROPHIL'])
path = "/Users/tylerrowe/Desktop/College/24Fall/Applied ML/AML-ClassifyingBloodImages/images"
# save the plot
plt.savefig(f'{path}/Distribution of White Blood Cells.png')

# print length of each category as well as the total number of images
# print('EOSINOPHIL: ', len(image_labels[image_labels['Mapped_Category'] == 'EOSINOPHIL']))
# print('LYMPHOCYTE: ', len(image_labels[image_labels['Mapped_Category'] == 'LYMPHOCYTE']))
# print('MONOCYTE: ', len(image_labels[image_labels['Mapped_Category'] == 'MONOCYTE']))
# print('NEUTROPHIL: ', len(image_labels[image_labels['Mapped_Category'] == 'NEUTROPHIL']))
# print('Total multiple WBC: ', len(image_labels[image_labels['Multiple_WBC'] == True]))
# print('Total: ', len(image_labels))
# Output:
#   EOSINOPHIL:  91
#   LYMPHOCYTE:  34
#   MONOCYTE:  22
#   NEUTROPHIL:  217
#   Total multiple WBC:  15
#   Total:  411

# Show the plot
# plt.show()

# save the plot
# plt.savefig('Distribution of White Blood Cells.png')

