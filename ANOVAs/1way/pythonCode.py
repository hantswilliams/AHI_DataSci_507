#### Good walkthrough: 
# https://www.pythonfordatascience.org/anova-python/ 

## Template 
import scipy.stats as stats
stats.f_oneway(df['dataColumn'][df['categoryColumn'] == 'category1'],
               df['dataColumn'][df['categoryColumn'] == 'category2'],
               df['dataColumn'][df['categoryColumn'] == 'category3'])

## Post-hoc analysis for significant differences between groups
# TUKEY HONESTLY SIGNIFICANT DIFFERENCE (HSD)
import statsmodels.stats.multicomp as mc
comp = mc.MultiComparison(df['dataColumn'], df['categoryColumn'])
post_hoc_res = comp.tukeyhsd()
post_hoc_res.summary()




## Example data:

df = pd.read_csv("https://raw.githubusercontent.com/researchpy/Data-sets/master/difficile.csv")
df.drop('person', axis= 1, inplace= True)
df['dose'].replace({1: 'placebo', 2: 'low', 3: 'high'}, inplace= True) # Recoding value from numeric to string
df.info()

import pandas as pd
import researchpy as rp

import scipy.stats as stats

stats.f_oneway(df['libido'][df['dose'] == 'high'],
               df['libido'][df['dose'] == 'low'],
               df['libido'][df['dose'] == 'placebo'])


