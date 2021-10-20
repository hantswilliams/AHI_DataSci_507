


###### 1 SAMPLE T-TEST ######
# To compare the mean of 1 group to a specific value, use the t.test() function.
# In a one-sample t-test, you compare the data from one group of data to some hypothesized mean. 
# For example, if someone said that diabetics on average take 3 medications, we could conduct a one-sample test comparing 
# the data from a sample of diabetic patients to a hypothesized mean of 3. 

#mu = expected/hypothesized mean 

t.test(x = dataframename$drugcountcolumn,  mu = 5)   




###### 2 SAMPLE T-TESTS ######

## Example dataset: 

# build in dataset 
## defult column names: extra, group, ID
sleep 


# also creating wide-version of `sleep` dataset
sleep_wide <- data.frame(
    ID=1:10,
    group1=sleep$extra[1:10],
    group2=sleep$extra[11:20]
)

sleep_wide



## INDEPENDENT (UNAPAIRED)
# Comparing two groups: INDEPENDENT two-sample t-test
# Welch t-test
t.test(extra ~ group, sleep)


## DEPENDENT (PAIRED)
# Sort by group then ID
sleep <- sleep[order(sleep$group, sleep$ID), ]
t.test(extra ~ group, sleep, paired=TRUE)


## PERFORMING WITH WIDE DATASET - 
t.test(sleep.wide$group1 - sleep.wide$group2)
