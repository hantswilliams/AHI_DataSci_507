### Linearity 
p1 <- ggplot(lin_reg, aes(.fitted, .resid)) + geom_point()
p1 <- p1 + stat_smooth(method="loess") + geom_hline(yintercept=0, col="red", linetype="dashed")
p1 <- p1 + xlab("Predicted") + ylab("Residuals")
p1 <- p1 + ggtitle("Residuals vs. Predicted Values") + theme_bw()

df_plt <- data.frame("fitted" = fitted(lin_reg), "observed" = X$medv)
p2 <- ggplot(df_plt, aes(x=fitted, y=observed)) + geom_point()
p2 <- p2 + stat_smooth(method="loess") + geom_abline(intercept = 1, col="red", linetype="dashed")
p2 <- p2 + xlab("Predicted") + ylab("Observed")
p2 <- p2 + ggtitle("Observed vs. Predicted Values") + theme_bw()

grid.arrange(p2, p1, ncol=2)




### Expectation (mean) of residuals is zero
mean(lin_reg$resid)



### No (perfect) multicollinearity
library(car)
vif(lin_reg)



#### Homoscedasticity (equal variance) of residuals
library(lmtest)

par(mfrow=c(2,2))  # set 2 rows and 2 column plot layout
plot(lin_reg)
print(bptest(lin_reg, data = X, studentize = TRUE)) # Breusch-Pagan test
print(gqtest(lin_reg)) # Goldfeld-Quandt



### No autocorrelation of residuals
library(ggplot2)
library(lmtest)

acf(lin_reg$residuals)  
dwtest(lin_reg)



### The features and residuals are uncorrelated
for (i in 1:(dim(X)[2])){
    cor_test <- cor.test(X[, i], lin_reg$residuals)  # 
    print(paste('Variable:', colnames(X)[i], 
                '--- correlation:', as.character(cor_test$estimate), 
                ', p-value:', as.character(cor_test$p.value), sep = " ", collapse = NULL))
    }


### There must be some variability in features
library(caret)
apply(X, 2, var)
nearZeroVar(X, saveMetrics= TRUE)
