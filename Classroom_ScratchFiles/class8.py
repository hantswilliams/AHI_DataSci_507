#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 18:26:24 2021

@author: hantswilliams
"""

import pandas as pd

diabetes = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/AHI_DataSci_507/main/Datasets/Diabetes/DB1_Diabetes/diabetic_data.csv')

diabetes_small = diabetes.sample(100)

### generate list of var names 
list(diabetes_small)


diabetes['totalCountProcedures'] = diabetes['num_procedures'] + diabetes['num_lab_procedures']


# time_in_hospital
# num_lab_procedures
# num_procedures (non lab)
# num_medications
# number_diagnoses


## Corr question 1: 
## Is there a correlation between time in hospital and the number 
## of lab procedures? 


## Corr question 2: 
## Is there a correlation between the number of diagnoses and the 
## number of total procedures (lab + unknown procedures)? 




## Question 1 
timeinhospital = diabetes['time_in_hospital']
labprocedures = diabetes['num_lab_procedures'] 


## Now lets do some statistical assumption checks: 
from scipy.stats import shapiro
import scipy.stats as stats
from matplotlib import pyplot

shapiro(timeinhospital)

timeinhospita_stat, timeinhospita_p = shapiro(timeinhospital)
labprocedures_stat, labprocedures_p = shapiro(labprocedures)

pyplot.hist(timeinhospital).show()
pyplot.hist(labprocedures).show()

print('normality checks passed......')


## Now lets do some checks for homogeneity 

#This way...is only calling in our variables that have 
#already been extracted from our original dataframe
#stats.bartlett('va1', 'var2') 

stats.bartlett(timeinhospital, labprocedures) 
stats.bartlett(diabetes['time_in_hospital'], diabetes['num_lab_procedures'] ) 



## Barlett failed -> was statistically significant for differences in residual 
## variation between time in hospital and num/lab-procedures BUT the shapiro
## passed -> so we will perform both tests 

# Pearson 
from scipy.stats import spearmanr, pearsonr

pearsoncorrelation, pearsonp = pearsonr(timeinhospital, labprocedures)
spearmancorrelation, spearmanp = spearmanr(timeinhospital, labprocedures)

pearonOutput = pd.DataFrame({'Correlation': pearsoncorrelation, 
                               'PValue': pearsonp, 'CorrType' : 'Pearson',
                               'From' : 'SciPy'}, index=[0])

spearmanOutput = pd.DataFrame({'Correlation': spearmancorrelation, 
                               'PValue': spearmanp, 'CorrType' : 'Spearman',
                               'From' : 'SciPy'}, index=[0])


## Example 2 - from PANDAS - PEARON and SPEARMAN CORRELATIONS
pdpearson = diabetes['time_in_hospital'].corr(diabetes['num_lab_procedures'], method='pearson')
pearonOutputPD = pd.DataFrame({'Correlation': pdpearson, 
                               'PValue': 'Not provided', 'CorrType' : 'Pearson',
                               'From' : 'Pandas'}, index=[0])


pdspearman = diabetes['time_in_hospital'].corr(diabetes['num_lab_procedures'], method='spearman')
spearmanOutputPD = pd.DataFrame({'Correlation': pdspearman, 
                               'PValue': 'Not provided', 'CorrType' : 'Spearman',
                               'From' : 'Pandas'}, index=[0])



corrOutput = pd.concat([pearonOutput, spearmanOutput, pearonOutputPD, spearmanOutputPD])





###### Example 2 
## Corr question 2: 
## Is there a correlation between the number of diagnoses and the 
## number of total procedures (lab + unknown procedures)? 

## Gut check 
diabetes['number_diagnoses'].describe()
diabetes['totalCountProcedures'].describe()


diabetes['number_diagnoses'].value_counts()
diabetes['totalCountProcedures'].value_counts()




## Question 1 
number_diagnoses = diabetes['number_diagnoses']
totalCountProcedures = diabetes['totalCountProcedures'].array


number_diagnoses_stat, number_diagnoses_p = shapiro(number_diagnoses)
totalCountProcedures_stat, totalCountProcedures_p = shapiro(totalCountProcedures)

# pyplot.hist(number_diagnoses).show()
# pyplot.hist(totalCountProcedures).show()
diabetes['number_diagnoses'].hist(bins=20)
diabetes['totalCountProcedures'].hist(bins=20)


stats.bartlett(timeinhospital, labprocedures) 
stats.bartlett(diabetes['time_in_hospital'], diabetes['num_lab_procedures'] ) 


pearsoncorrelation, pearsonp = pearsonr(number_diagnoses, totalCountProcedures)
spearmancorrelation, spearmanp = spearmanr(number_diagnoses, totalCountProcedures)













