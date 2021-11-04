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
import seaborn as sns


heartfailure = pd.read_csv('/Users/hantswilliams/Dropbox/Biovirtua/Python_Projects/ahi/AHI_DataSci_507/Datasets/HeartDisease/heart.csv')


# DV = cholesterol  // chol 


# IV Factor 1 = chestpain // cp - 

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
thal: A blood disorder called thalassemia 
Value 0: NULL (dropped from the dataset previously
Value 1: fixed defect (no blood flow in some part of the heart)
Value 2: normal blood flow
Value 3: reversible defect (a blood flow is observed but it is not normal)
"""

workingdf = heartfailure[['chol', 'thal', 'cp']]


workingdf['thal'] = workingdf['thal'].astype(str)
workingdf['cp'] = workingdf['cp'].astype(str)


descriptives = workingdf.describe()

thal_counts = workingdf['thal'].value_counts().reset_index()
cp_counts = workingdf['cp'].value_counts().reset_index()



# generate a boxplot to see the data distribution by genotypes and years. Using boxplot, we can easily detect the 
# differences between different groups
sns.boxplot(x="cp", y="chol", hue="thal", data=heartfailure, palette="Set3") 


import statsmodels.api as sm
from statsmodels.formula.api import ols

ols('chol ~ C(thal) + C(cp)', data=workingdf).fit()
model = ols('chol ~ C(thal) + C(cp)', data=workingdf).fit()

anova_table = sm.stats.anova_lm(model, typ=2)
anova_table


model2 = ols('chol ~ C(thal) + C(cp) + C(thal):C(cp)', data=workingdf).fit()
anova_table2 = sm.stats.anova_lm(model2, typ=2)
anova_table2




from bioinfokit.analys import stat
# perform multiple pairwise comparison (Tukey HSD)
# unequal sample size data, tukey_hsd uses Tukey-Kramer test
res = stat()
res.tukey_hsd(df=workingdf, res_var='chol', xfac_var='cp', 
              anova_model='chol~C(cp)+C(thal)+C(cp):C(thal)')
res.tukey_summary







# QQ-plot
import statsmodels.api as sm
import matplotlib.pyplot as plt
# res.anova_std_residuals are standardized residuals obtained from two-way ANOVA (check above)
sm.qqplot(res.anova_std_residuals, line='45')
plt.xlabel("Theoretical Quantiles")
plt.ylabel("Standardized Residuals")
plt.show()

# histogram
plt.hist(res.anova_model_out.resid, bins='auto', histtype='bar', ec='k') 
plt.xlabel("Residuals")
plt.ylabel('Frequency')
plt.show()

# Shapiro-Wilk test
import scipy.stats as stats
w, pvalue = stats.shapiro(res.anova_model_out.resid)
print(w, pvalue)

# if you have  a stacked table, you can use bioinfokit v1.0.3 or later for the Levene's test
from bioinfokit.analys import stat 
res = stat()
res.levene(df=d_melt, res_var='value', xfac_var=['Genotype', 'years'])
res.levene_summary

#interpretation: As the p value (0.09) is non-significant, we fail to reject the null 
# hypothesis and conclude that treatments have equal variance














