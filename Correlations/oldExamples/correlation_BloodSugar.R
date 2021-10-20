## Hollander & Wolfe (1973), p. 187f.
## Assessment of tuna quality.  We compare the Hunter L measure of
##  lightness to the averages of consumer panel scores (recoded as
##  integer values from 1 to 6 and averaged over 80 such values) in
##  9 lots of canned tuna.

morningbloodsugar <- c(100, 98, 115, 100, 84, 114, 119, 120, 150) #blood sugar levels morning 
eveningbloodsugar <- c( 113,  115,  114,  130,  100,  78,  93,  97,  100) #bloog sugar levels in evening

#1 is there a linear relationship between these two sets of data ? 
plot(morningbloodsugar, eveningbloodsugar)
# FAILED - visually, does not appear to be a linear relationship between morning and evening bloog sugar

#2 normal distrubrition 
morningBSmean <- mean(morningbloodsugar)
morningBSsd = sd(morningbloodsugar)

eveningBSmean <- mean(eveningbloodsugar)
eveningBSsd = sd(eveningbloodsugar)
# MAYBE PASSED - MEANS are larger then the SD's 

# Homogeneity of Variance 
bartlett.test(eveningbloodsugar ~ morningbloodsugar)

# FAILED homogeneity of variance 

# -> next steps -> performing a NON-PARAMETRIC Correlation Test 
# Pearson - OUT 
# Spearman / Kendell to chooses from 

spearmanOutput = cor.test(morningbloodsugar, eveningbloodsugar,
         method = c("spearman"),
         conf.level = 0.95)




##  The alternative hypothesis of interest is that the
##  Hunter L value is positively associated with the panel score.

cor.test(x, y, method = "kendall", alternative = "greater")
## => p=0.05972

cor.test(x, y, method = "kendall", alternative = "greater",
         exact = FALSE) # using large sample approximation
## => p=0.04765

## Compare this to
cor.test(x, y, method = "spearm", alternative = "g")
cor.test(x, y,                    alternative = "g")

## Formula interface.
require(graphics)
pairs(USJudgeRatings)
cor.test(~ CONT + INTG, data = USJudgeRatings)