# Analysis for variance (1-way ANOVA) in R 

res.aov <- aov(numericalColumn ~ grouperColumn, data = yourDataframe)
summary(res.aov)

## Tukey HSD post-hoc analysis 
TukeyHSD(res.aov)




# Non-parametric: when no homogeneity (equal variance): 
oneway.test(weight ~ group, data = my_data)
# Posthoc for above: 
pairwise.t.test(my_data$weight, my_data$group, p.adjust.method = "BH", pool.sd = FALSE)


# Non-parametric: 
kruskal.test(DV ~ IVfactor, data = clean_nomiss)


# Non-parametric / tuskey equivalent / 
library(userfriendlyscience)
games.howell(df$var1, df$var2) 

## 