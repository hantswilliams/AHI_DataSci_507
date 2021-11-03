import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv("https://reneshbedre.github.io/assets/posts/anova/plants_leaves.csv")
df_melt = pd.melt(df.reset_index(), id_vars=['Id'], value_vars=['W1', 'W2', 'W3', 'W4', 'W5'])

ax = sns.boxplot(x='time_points', y='leaves', data=df_melt, color='#99c2a2')
ax = sns.swarmplot(x="time_points", y="leaves", data=df_melt, color='#7d0013')
plt.show()

#Perform 1-way repeated ANOVA 

# install pingouin as !pip install pingouin
# if using google colab: !pip install pingouin
import pingouin as pg
res = pg.rm_anova(dv='leaves', within='time_points', subject='Id', data=df_melt, detailed=True)
res

## Post-hoc tests for repeated 1-way 
post_hocs = pg.pairwise_ttests(dv='leaves', within='time_points', subject='Id', padjust='fdr_bh', data=df_melt)
post_hocs


## repeated measure ANOVA assumptions 

# Spherecity / Homongeneity of variance 
# Assumption of sphericity
# The assumption of sphericity can be tested using Mauchly’s test of sphericity. 
# The violation of the assumption of sphericity can lead to an increase in type II error 
# (loss of statistical power) and the F value is not valid.
import pingouin as pg
pg.sphericity(data=df_melt, dv='leaves', subject='Id', within='time_points')[-1]

# Interpretation -> 
# If the p value is greater than .05 (e.g., 0.8883) this means non-significant (p > 0.05), the data met the assumption of sphericity, 
# and variances of differences of independent variables are equal and met 

# Normality 
# install pingouin as !pip install pingouin
pg.normality(data=df_melt, dv='leaves', group='time_points')

# Shapiro-Wilk test can be used for checking the assumption for normality of each 
# level of the within-subjects factor