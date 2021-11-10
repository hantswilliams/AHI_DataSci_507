### Basic Regression 


lin_reg <- lm(y ~ ., data = cbind(X, y))
summary(lin_reg)

