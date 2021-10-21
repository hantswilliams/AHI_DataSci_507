###### 1 SAMPLE T-TEST ######
###### 1 SAMPLE T-TEST ######
###### 1 SAMPLE T-TEST ######
###### 1 SAMPLE T-TEST ######

# https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ttest_1samp.html

from scipy.stats import ttest_1samp
ttest_1samp(dataarray, expectedmeanValue)










###### 2 SAMPLE T-TESTS ######
###### 2 SAMPLE T-TESTS ######
###### 2 SAMPLE T-TESTS ######
###### 2 SAMPLE T-TESTS ######

# Example data: 
import pandas as pd
data = {'Category': ['cat2','cat1','cat2','cat1','cat2','cat1','cat2','cat1','cat1','cat1','cat2'],
        'values': [1,2,3,1,2,3,1,2,3,5,1]}
my_data = pd.DataFrame(data)



# Independent t-test // TWO INDEPENDENT SAMPLES OF SCORES (ASSUMES equal VARIANCE)

from scipy.stats import ttest_ind

cat1 = my_data[my_data['Category']=='cat1']
cat2 = my_data[my_data['Category']=='cat2']

ttest_ind(cat1['values'], cat2['values']) #returns t-statistics and the p-value 


# Dependent t-test // TWO RELATED SAMPLES OF SCORES (ASSUMES equal VARIANCE)

from scipy.stats import ttest_rel

cat1 = my_data[my_data['Category']=='cat1']
cat2 = my_data[my_data['Category']=='cat2']

ttest_rel(cat1['values'], cat2['values']) #returns t-statistics and the p-value 