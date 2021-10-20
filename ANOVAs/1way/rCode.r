# Analysis for variance (1-way ANOVA) in R 

res.aov <- aov(numericalColumn ~ grouperColumn, data = yourDataframe)
summary(res.aov)

## Tukey HSD post-hoc analysis 
TukeyHSD(res.aov)


