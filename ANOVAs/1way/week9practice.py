#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 16:27:46 2021

@author: hantswilliams
"""



import pandas as pd
import numpy as np 

diabetes = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/AHI_DataSci_507/main/Datasets/Diabetes/DB1_Diabetes/diabetic_data.csv')

diabetes_small = diabetes.sample(100)


## Data transformation step 

diabetes = diabetes.replace('?', np.NaN)



### generate list of var names 
list(diabetes_small)


# 1 factor of RACE has 6 levels: 
    
# Lets replace nan for diabetes.race with 'Other'

diabetes['race'] = diabetes['race'].replace(np.NaN, 'Other')    
    
diabetes.race.value_counts()
diabetes['race'].value_counts() 

# 1 factor of AGE we have 10 levels 
diabetes.age.value_counts() 
diabetes['age'].value_counts() 

# 1 factor of PAYER_CODE we have 17 levels 
diabetes.payer_code.value_counts()
len(diabetes.payer_code.value_counts())

# 1 factor of medical_specialty we have 72 levels 
diabetes.medical_specialty.value_counts()
len(diabetes.medical_specialty.value_counts())

specialtycounts = pd.DataFrame(diabetes.medical_specialty.value_counts())      
specialtycounts = specialtycounts.reset_index()


#### Continuous values: 
    
timeinhospital = diabetes['time_in_hospital']
labprocedures = diabetes['num_lab_procedures'] 




# 1 way anova 
# 1 DV 
# 1 IV - 




















