## Correlations 

## Example 1 - SCIPY package - PEARSON and SPEARMAN CORRELATIONS
# https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.spearmanr.html
# https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.pearsonr.html
from scipy.stats import spearmanr, pearsonr
corr, _ = spearmanr(data1, data2)

## Example 2 - from PANDAS - PEARON and SPEARMAN CORRELATIONS
# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.corr.html
import pandas as pd
df['var1'].corr(df['var2'], method='pearson')
df['var1'].corr(df['var2'], method='spearman')

