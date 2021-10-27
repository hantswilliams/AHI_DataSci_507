## Parametric assumptions
## https://www.pythonfordatascience.org/parametric-assumptions-python/
## https://machinelearningmastery.com/a-gentle-introduction-to-normality-tests-in-python/ 

"""

Parametric test assumptions

Independence
Population distributions are normal
Samples have equal variances

"""


### 1 Independence

"""

INDEPENDENCE
This assumption is checked during the setup of the study. It means that each observation is 
independent of another; if there are 2 or more groups being compared, then it refers to that 
fact that groups are mutually exclusive, i.e. each individual belongs to only 1 group; and that 
the data is not repeated over time.

If data is repeated measures, longitudinal/panel or time series, there are appropriate methods 
to account for the repeated data points from individuals. This is typically handled in 
the math of the statistical test that is designed to analyze this type of data.

"""


### 2 NORMALITY

"""

The normality assumption is applied differently depending on the statistical method being used. 
For example, it applies to the shape of the sampling distribution for the dependent variable (outcome variable) 
if it's a univariate test, to the difference scores if it's mean comparison 
(ex. independent sample t-test or paired t-test), or to the residuals if it's a regression framework. 
This assumption can be checked with a formal TEST or GRAPHICALLY. 

"""


#### 2A Normality Tests

# Shapiro-Wilk Test - UNIVARIATE TEST / correlation 
from numpy.random import seed
from numpy.random import randn
from scipy.stats import shapiro
# seed the random number generator
seed(1)
# generate univariate observations
data = 5 * randn(100) + 50
# normality test
stat, p = shapiro(data)
print('Statistics=%.3f, p=%.3f' % (stat, p))
# interpret
alpha = 0.05
if p > alpha:
	print('Sample looks Gaussian (fail to reject H0)')
else:
	print('Sample does not look Gaussian (reject H0)')


# Shapiro-Wilk (SW) Test for independent t-test framework 

import pandas as pd
import scipy.stats as stats

df = pd.read_csv("https://raw.githubusercontent.com/researchpy/Data-sets/master/blood_pressure.csv")

sampling_difference = df['bp_after'][df['sex'] == 'Male'].values - df['bp_after'][df['sex'] == 'Female'].values

stats.shapiro(sampling_difference)

# Expected output above: (0.98586106300354, 0.7147841453552246)


# From regression or ANOVA framework
import pandas as pd
import scipy.stats as stats
import statsmodels.formula.api as smf

df = pd.read_csv("https://raw.githubusercontent.com/researchpy/Data-sets/master/blood_pressure.csv")

model = smf.ols("bp_after ~ C(sex) + C(agegrp)", data= df).fit()

stats.shapiro(model.resid)

# Expected output from above: (0.9816310405731201, 0.10094476491212845)



# Kolmogorov-Smirnov (KS) Test
# The null hypothesis is that the data is normal (matches compared distribution). 
# # The Kolmogorov-Smirnov test is a distance test (D'Agostino, 1971). It evaluates normality 
# # by comparing the data's empirical distribution function to the expected cumulative distribution 
# # function of the comparison distribution (Öztuna D., Elhan A., & Tüccar, 2006).

# Coming from independent t-test framework

import pandas as pd
import scipy.stats as stats

df = pd.read_csv("https://raw.githubusercontent.com/researchpy/Data-sets/master/blood_pressure.csv")

stats.ks_2samp(df['bp_after'][df['sex'] == 'Male'],
               df['bp_after'][df['sex'] == 'Female'])

# Expected output: Ks_2sampResult(statistic=0.3666666666666667, pvalue=0.00041326763403322234)


# From regression or ANOVA framework

import pandas as pd
import scipy.stats as stats
import statsmodels.formula.api as smf

df = pd.read_csv("https://raw.githubusercontent.com/researchpy/Data-sets/master/blood_pressure.csv")

model = smf.ols("bp_after ~ C(sex) + C(agegrp)", data= df).fit()

stats.kstest(model.resid, 'norm')

# Expected output: KstestResult(statistic=0.4502179708439199, pvalue=1.0174625716715393e-22)







### 2B Noramlity: Graphical tests 
# Probability Plot

# The probability plot plots the ordered data against the theoretical distribution. 
# # The better the ordered data fits the theoretical distribution, the less deviation there will 
# # be from the fit line that is in the middle of the graph.


# Simple univariate 
# histogram plot
from numpy.random import seed
from numpy.random import randn
from matplotlib import pyplot
# seed the random number generator
seed(1)
# generate univariate observations
data = 5 * randn(100) + 50
# histogram plot
pyplot.hist(data)
pyplot.show()



# Coming from mean comparison framework (independent sample t-test)
import pandas as pd
import scipy.stats as stats

df = pd.read_csv("https://raw.githubusercontent.com/researchpy/Data-sets/master/blood_pressure.csv")

sampling_difference = df['bp_after'][df['sex'] == 'Male'] - \
                      df['bp_after'][df['sex'] == 'Female']

fig = plt.figure(figsize= (10, 10))
ax = fig.add_subplot(111)

normality_plot, stat = stats.probplot(sampling_difference, plot= plt, rvalue= True)
ax.set_title("Probability plot of sampling difference \n with R value")
ax.set

plt.show()


# From regression or ANOVA framework

import pandas as pd
import scipy.stats as stats
import statsmodels.formula.api as smf

df = pd.read_csv("https://raw.githubusercontent.com/researchpy/Data-sets/master/blood_pressure.csv")

model = smf.ols("bp_after ~ C(sex) + C(agegrp)", data= df).fit()

fig = plt.figure(figsize= (10, 10))
ax = fig.add_subplot(111)

normality_plot, stat = stats.probplot(model.resid, plot= plt, rvalue= True)
ax.set_title("Probability plot of regression residuals \n with R value")
ax.set

plt.show()


#WHAT IF NORMALITY IS VIOLATED?
#If the assumption of normality is violated fear not! There are a few routes to consider, these are in no particular order:
#Rely on the Central Limit Theorem if the sample size is large enough ()
#Use a non-parametric statistical test
#Transform the data



# Quantile-Quantile Plot
# The function takes the data sample and by default assumes we are comparing it 
# to a Gaussian distribution. We can draw the standardized line by setting the ‘line‘ argument to ‘s‘.
# QQ Plot
from numpy.random import seed
from numpy.random import randn
from statsmodels.graphics.gofplots import qqplot
from matplotlib import pyplot
# seed the random number generator
seed(1)
# generate univariate observations
data = 5 * randn(100) + 50
# q-q plot
qqplot(data, line='s')
pyplot.show()




# Kurtosis 

## scipy 
from scipy.stats import norm, kurtosis
data = norm.rvs(size=1000, random_state=3)
kurtosis(data)

## pandas 
pd.DataFrame(x).skew()


# Skewness

## scipy 
from scipy.stats import skew
skew([1, 2, 3, 4, 5])
0.0

## pandas 
pd.DataFrame(x).kurtosis()
 













# 3 HOMOGENEITY OF VARIANCES

# As with testing the assumption of normality, there are a few statistical tests available to test the assumption of equal variances. 
# Some common methods are the Barlett test and Levene's test for equality of variances. Choosing the correct test is also dependent on 
# the assumption of normality. For example, Barlett's test has been found to be sensitive to departures from normality whereas 
# Levene's test is less sensitive to this (Conover, 1981).

#Barlett's Test
# Barlett's test is used to test if the groups, which can be referred to as k, have equal variances. Barlett's test can 
# test for equality between 2 or more groups.

import pandas as pd
import scipy.stats as stats

df = pd.read_csv("https://raw.githubusercontent.com/researchpy/Data-sets/master/blood_pressure.csv")

stats.bartlett(df['bp_after'][df['sex'] == 'Male'],
               df['bp_after'][df['sex'] == 'Female'])

# Expected output: BartlettResult(statistic=3.9379638422812793, pvalue=0.047207884641474476)



# Levene's Test
# Levene's test tests if the different goups have equal variances (Levene, 1960). Levene's test is less 
# sensitive than Barlett's test to departures from normality and power (Conover, 1981). Levene's test of homogeneity 
# of variances can test for equality between 2 or more groups. 

import pandas as pd
import scipy.stats as stats

df = pd.read_csv("https://raw.githubusercontent.com/researchpy/Data-sets/master/blood_pressure.csv")

# Using the mean

stats.levene(df['bp_after'][df['sex'] == 'Male'],
             df['bp_after'][df['sex'] == 'Female'])

# Expected output: LeveneResult(statistic=5.0464151793144625, pvalue=0.026537264851214513)


# WHAT IF HOMOGENEITY OF VARIANCES IS VIOLATED?
# If there is not equal variances between groups there are a few routes to consider, these are in no particular order:
# Use a non-parametric statistical test
# Transform the data
# Common data transformation methods will be provided in the next section.