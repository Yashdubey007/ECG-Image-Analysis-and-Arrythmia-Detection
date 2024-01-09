# ECG-Image-Analysis-and-Arrythmia-Detection

This Project is used to analyse ECG Image and detect the arrythmia in ECG graph image. The dataset contains ECG images data from Kaggle https://www.kaggle.com/datasets/analiviafr/ecg-images. This dataset is composed of Electrocardiogram (ECG) images obtained from the database MIT-BIH Arrhythmia. For that, the ECG signals were pre-processed, generating 109.445 images with a resolution of 256x256. In sequence, five cardiac arrhythmia superclasses recommended by AAMI were selected for work.

ECG images dataset:
Number of Samples: 109445
Number of Categories: 5
Image Resolution: 256x256
Data Source: Physionet's MIT-BIH Arrhythmia Dataset
Classes: (N, S, V, Q, F)

N (Normal beat)	90.589
S (Supraventricular ectopic beat)	2.779
V (Ventricular ectopic beat)	7.236
F (Fusion beat)	803
Q (Unknown beat)	8.038

Also I took reference from Basic ECG interpretation article of Lisa Leonard FNP-C, ENP-C Departmental Lead Emergency Department PRISMA Health


preprocessor- This notebook preprocesses the image and is used for training and testing of the model. It has the accuracy of 89%.

saved_model- This is the customized CNN model that is designed by me.

app- This file has the code for designing web app.
 
