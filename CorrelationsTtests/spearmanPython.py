#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 20:28:16 2021

@author: hantswilliams
"""

import scipy
from scipy import stats
import pandas as pd

morningbloodsugar = [100, 98, 115, 100, 84, 114, 119, 120, 150] #blood sugar levels morning 
eveningbloodsugar = [113,  115,  114,  130,  100,  78,  93,  97,  100] #bloog sugar levels in evening

morningbloodsugar = {100, 98, 115, 100, 84, 114, 119, 120, 150} #blood sugar levels morning 
eveningbloodsugar = {113,  115,  114,  130,  100,  78,  93,  97,  100} #bloog sugar levels in evening



fakeOutput = scipy.stats.spearmanr(morningbloodsugar, eveningbloodsugar)


spearmanStatistic, pValue = scipy.stats.spearmanr(morningbloodsugar, eveningbloodsugar)

dataframe = pd.DataFrame({'spearmanStatistic': spearmanStatistic, "pValue": pValue}, index=[0])