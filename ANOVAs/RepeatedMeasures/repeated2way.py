import pandas as pd
# load data file
df=pd.read_csv("https://reneshbedre.github.io/assets/posts/anova/plants_leaves_two_within.csv")
df.head(2)

# In this dataset, there are two independent variables (time and year) and number of leaves (num_leaves)
# is a dependent variable

# generate a boxplot to see the data distribution by time points. Using boxplot, we can 
# boxplot helps detect the differences between different time points and find any outliers
import matplotlib.pyplot as plt
import seaborn as sns
sns.boxplot(x="time", y="num_leaves", hue="year", data=df, palette="Set3")
plt.show()

# install pingouin as !pip install pingouin
import pingouin as pg
res = pg.rm_anova(dv='num_leaves', within=['time', 'year'], subject='plants', 
                  data=df, detailed=True)
res