## Assumptions
# - Homogeneity of variance
# - Normal distribution of data
# - Independence

## Creating fake data
hb <- rnorm(100, mean = 15, sd = 3)
crp = rgamma(100, 2, 2)



### NORAMLITY 
## The assumption of normality
# This asumption is arguably of most importance. It can be checked visually or numerically. Histograms and quantile-quantile (QQ) 
# plots serve as visual markers and various statistical tests, such as the Shapiro-Wilk test, serves as numerical tests.


# Numerical tests
library(pastecs)
round(stat.desc(hb, basic = FALSE, norm = TRUE), digits = 3)

# SHAPIRO-WILK TEST FOR NORMALITY
# The Shapiro-Wilk test can be used on its own. A p value of less than 0.05 indicates a high likelihood that the 
# assumption for normality is NOT met. Below the hb and crp variables are passed as argument to the shapito.test() command, 
# resulting in the same test statistic and p value as above.
shapiro.test(hb)


# Visual tests 
# A histogram with default bin size is created to visualize the frequency distribution of the data. A kernel density estimate is 
# provided using the line() command.
hb <- rnorm(100, mean = 15, sd = 3)
hist(hb, prob = TRUE, main = "Histogram of hemoglobin values", las = 1, xlab = "Hemoglobin")
lines(density(hb))


# The QQ plot below plots the sample quantile of each data point value against its theoretical quantile. 
# A line is added for clarity. The closer the data point values follow the line, the more likely that our 
# assumption has been met.

qqnorm(hb, main = "QQ plot of hemoglobin values")
qqline(hb)



## Skewness and Kurtosis

kurtosis(variableofinterest)                # apply the kurtosis function
skewness(variableofinterest)                # apply the skewness function



### HOMOGENEITY OF VARIANCE
## The assumption of homogeneity of variance
# The Levene test is used to test for homogeneity of variance. The null hypothesis states equality of variances. 
# In order to conduct Levene’s test, the Companion to Applied Regression, car, package is required.
# The leveneTest() command requires the use of a data.frame object. The code below imports a csv file and prints 
# the first six rows and a summary to the screen. 

library(car)
leveneTest(df$CRP, df$Group, center = mean)
