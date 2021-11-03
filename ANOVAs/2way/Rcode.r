# Two-way - no interaction prediction 
two.way <- aov(DV ~ IV1 + IV2, data = yourdataframe)

# Two-way - with interaction prediction 
two.way <- aov(DV ~ IV1 * IV2, data = yourdataframe)

# Two-way - with interaction prediction 
two.way <- aov(DV ~ IV1 + IV2 + IV1:IV2, data = yourdataframe)




# Requires ‘car’ package
# Two-way - no interaction prediction 
two.way <- aov(DV ~ IV1 + IV2, data = yourdataframe) 
Anova(two.way, type=“III”)
Anova(two.way, type=“I”)

# Two-way - with interaction prediction 
two.way <- aov(DV ~ IV1 * IV2, data = yourdataframe)
Anova(two.way, type=“III”)
Anova(two.way, type=“I”)

# Two-way - with interaction prediction 
two.way <- aov(DV ~ IV1 + IV2 + IV1:IV2, data = yourdataframe)
Anova(two.way, type=“III”)
Anova(two.way, type=“I”)



# TUKEY 
TukeyHSD(two.way)
TukeyHSD(two.way, which=“IV1”)
TukeyHSD(two.way, which=“IV2”)
TukeyHSD(two.way, which=“IV1:IV2”)

