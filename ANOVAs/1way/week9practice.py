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


# 1 factor of RACE has 5 levels: 
    
# Lets replace nan for diabetes.race with 'Other'

diabetes['race'] = diabetes['race'].replace(np.NaN, 'Other')    
diabetes.race.value_counts()
diabetes['race'].value_counts() 
len(diabetes['race'].value_counts() )

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
# 1 DV - time_in_hospital
# 1 IV - Race 

# is there a difference between the "levels" of race 
# and time in hospital? 


### Checking assumptions....

# From regression or ANOVA framework
import pandas as pd
import scipy.stats as stats
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt
from scipy.stats import kurtosis, skew, bartlett


# DV ~ C(IV) + C(IV)
model = smf.ols("time_in_hospital ~ C(race)", data = diabetes).fit()
stats.shapiro(model.resid)



# Lets create a chart 

race1 = diabetes[diabetes['race'] == 'Caucasian']
race2 = diabetes[diabetes['race'] == 'AfricanAmerican']
race3 = diabetes[diabetes['race'] == 'Other']
race4 = diabetes[diabetes['race'] == 'Hispanic']
race5 = diabetes[diabetes['race'] == 'Asian']

plt.hist(race1['time_in_hospital'])
plt.show()

plt.hist(race2['time_in_hospital'])
plt.show()

plt.hist(race3['time_in_hospital'])
plt.show()

plt.hist(race4['time_in_hospital'])
plt.show()

plt.hist(race5['time_in_hospital'])
plt.show()



# kertosis 
print(kurtosis(race1['time_in_hospital']))
print(kurtosis(race2['time_in_hospital']))
print(kurtosis(race3['time_in_hospital']))
print(kurtosis(race4['time_in_hospital']))
print(kurtosis(race5['time_in_hospital']))

# skewness 
print('skew white: ', skew(race1['time_in_hospital']))
print('skew black: ', skew(race2['time_in_hospital']))
print(skew(race3['time_in_hospital']))
print(skew(race4['time_in_hospital']))
print(skew(race5['time_in_hospital']))


#### Homogeneity of Variance 
## barlett test 


stats.bartlett(race1['time_in_hospital'],
               race2['time_in_hospital'],
               race3['time_in_hospital'],
               race4['time_in_hospital'],
               race5['time_in_hospital']
               )






## Template 
stats.f_oneway(race1['time_in_hospital'],
               race2['time_in_hospital'],
               race3['time_in_hospital'],
               race4['time_in_hospital'],
               race5['time_in_hospital'])

## Post-hoc analysis for significant differences between groups
# TUKEY HONESTLY SIGNIFICANT DIFFERENCE (HSD)
import statsmodels.stats.multicomp as mc
comp = mc.MultiComparison(diabetes['time_in_hospital'], diabetes['race'])
post_hoc_res = comp.tukeyhsd()
tukey1way = pd.DataFrame(post_hoc_res.summary())



race1['time_in_hospital'].describe()
race2['time_in_hospital'].describe()
race5['time_in_hospital'].describe()




