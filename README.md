# Blood-Cell-Classification

We leverage Convolutional Neural Networks to propose a machine learning approach for the analysis of blood samples through image processing. The primary objective is to detect and classify individual cells within blood sample images, classifying the cells as either platelets, white blood cells (WBC), and red blood cells (RBC). The secondary objective further classifies WBC into specific subtypes: Eosinophils, Lymphocytes, Monoctyes and Neutrophils. The methodology implements convolutional neural networks (CNNs) for object detection and classification. We achieve 98.3 % accuracy for detection of WBCs, and 87.6 % accuracy in WBC subtype classification, showcasing the effectiveness of our proposed model in advancing automated hematological analysis. 

ResearchPaper.pdf contains a thorough writeup describing our methodology, experimentation, and results. 

FinalPresentation.pdf contains an overview of the project in power point format. 

The other files in the repository represent the code for data preprocessing and exploration, the object detection model trained using the YOLOv8 framework, and the classification model trained using ResNet50. Additionally, the BoundingBoxModel folder contains the predicted bounding box coordinates and annotated images for the training, validation, and testing sets. It also includes the weights for the most successful YOLOv8 model. 

Objective 1 Dataset (Bounding Box Model):
https://github.com/Shenggan/BCCD_Dataset

Objective 2 Dataset (WBC Classification):
https://www.kaggle.com/datasets/paultimothymooney/blood
