
library(dplyr)

diabetes = read.csv('https://raw.githubusercontent.com/hantswilliams/AHI_DataSci_507/main/Datasets/Diabetes/DB1_Diabetes/diabetic_data.csv')
diabetes_small = sample_n(diabetes, 10)