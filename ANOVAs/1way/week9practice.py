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

# 1 factor of AGE 
diabetes.age.value_counts() 
diabetes['age'].value_counts() 






