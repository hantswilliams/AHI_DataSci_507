#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 19:29:11 2021

@author: hantswilliams


age
sex
chest pain type (4 values)
resting blood pressure
serum cholestoral in mg/dl
fasting blood sugar > 120 mg/dl
resting electrocardiographic results (values 0,1,2)
maximum heart rate achieved
exercise induced angina
oldpeak = ST depression induced by exercise relative to rest
the slope of the peak exercise ST segment
number of major vessels (0-3) colored by flourosopy
thal: 3 = normal; 6 = fixed defect; 7 = reversable defect


"""

import pandas as pd 


heartfailure = pd.read_csv('/Users/hantswilliams/Dropbox/Biovirtua/Python_Projects/ahi/AHI_DataSci_507/Datasets/HeartDisease/heart.csv')


# DV = cholesterol  // chol 
# IV Factor 1 = chestpain // CP - 

"""
-- Value 1: typical angina
-- Value 2: atypical angina
-- Value 3: non-anginal pain
-- Value 4: asymptomatic
"""


# IV Factor 2 = // thal - 
"""
3 = normal; 6 = fixed defect; 7 = reversable defect
"""

"""
thal: A blood disorder called thalassemia Value 0: NULL (dropped from the dataset previously
Value 1: fixed defect (no blood flow in some part of the heart)
Value 2: normal blood flow
Value 3: reversible defect (a blood flow is observed but it is not normal)
"""























