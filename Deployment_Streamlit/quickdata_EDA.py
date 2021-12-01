#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 10:37:43 2020

@author: hantswilliams

# Datafrom: https://console.cloud.google.com/marketplace/product/hhs/medicare

"""

import pandas as pd



# from google.cloud import bigquery
# import pandas_gbq
# from google.oauth2 import service_account



# credentials = service_account.Credentials.from_service_account_file(
#     '/Users/hantswilliams/Documents/local_important/pem_files/CampusPO Login-db33e522aedb.json',
# )

# query1 = """SELECT * FROM `bigquery-public-data.cms_medicare.hospital_general_info`"""
# query2 = """SELECT * FROM `bigquery-public-data.cms_medicare.inpatient_charges_2015`"""
# query3 = """SELECT * FROM `bigquery-public-data.cms_medicare.outpatient_charges_2015`"""

# hospitals = pandas_gbq.read_gbq(query1, project_id="moonlit-triumph-864", credentials=credentials)
# inpatient = pandas_gbq.read_gbq(query2, project_id="moonlit-triumph-864", credentials=credentials)
# outpatient = pandas_gbq.read_gbq(query3, project_id="moonlit-triumph-864", credentials=credentials)

df_hospital = pd.read_csv("/Users/hantswilliams/Dropbox/Biovirtua/Python_Projects/ahi/AHI_STATS_507/Week13_Summary/hospital_info.csv")
df_inpatient = pd.read_csv("/Users/hantswilliams/Dropbox/Biovirtua/Python_Projects/ahi/AHI_STATS_507/Week13_Summary/inpatient_2015.csv")
df_outpatient = pd.read_csv("/Users/hantswilliams/Dropbox/Biovirtua/Python_Projects/ahi/AHI_STATS_507/Week13_Summary/outpatient_2015.csv")






########################################################################################################################
########################################################################################################################
########################################################################################################################
#### EDA // what is there for each: 
    
# Pandas Profiling 
from pandas_profiling import ProfileReport

profile1 = ProfileReport(df_hospital, explorative=True)
profile1.to_file("/Users/hantswilliams/Dropbox/Biovirtua/Python_Projects/ahi/AHI_STATS_507/Week13_Summary/output/profiling_df_hospital.html")

profile2 = ProfileReport(df_outpatient, explorative=True)
profile2.to_file("/Users/hantswilliams/Dropbox/Biovirtua/Python_Projects/ahi/AHI_STATS_507/Week13_Summary/output/profiling_df_outpatient.html")



# Sweet Viz 
import sweetviz as sv

sweet_report1 = sv.analyze(df_hospital)
sweet_report1.show_html('/Users/hantswilliams/Dropbox/Biovirtua/Python_Projects/ahi/AHI_STATS_507/Week13_Summary/output/sweet_report_df_hospital.html')

sweet_report2 = sv.analyze(df_outpatient)
sweet_report2.show_html('/Users/hantswilliams/Dropbox/Biovirtua/Python_Projects/ahi/AHI_STATS_507/Week13_Summary/output/sweet_report_df_outpatient.html')

sweet_report3 = sv.analyze(df_inpatient)
sweet_report3.show_html('/Users/hantswilliams/Dropbox/Biovirtua/Python_Projects/ahi/AHI_STATS_507/Week13_Summary/output/sweet_report_df_inpatient.html')



# D-tale
import dtale 

d = dtale.show(df_hospital, ignore_duplicate=True)
d.open_browser()

d = dtale.show(df_inpatient, ignore_duplicate=True)
d.open_browser()
########################################################################################################################
########################################################################################################################
########################################################################################################################







########################################################################################################################
########################################################################################################################
########################################################################################################################
### Automatic Data Cleaning 

from janitor import clean_names, remove_empty

# This cleans the column names as well as removes any duplicate rows
df_hospital_2 = clean_names(df_hospital)
df_hospital_2 = remove_empty(df_hospital_2)

df_inpatient_2 = clean_names(df_inpatient)
df_inpatient_2 = remove_empty(df_inpatient_2)

df_outpatient_2 = clean_names(df_outpatient)
df_outpatient_2 = remove_empty(df_outpatient_2)



### Save the cleaned datasets for visualization: 

df_hospital_2.to_csv('/Users/hantswilliams/Dropbox/Biovirtua/Python_Projects/ahi/df_hospital_2.csv', index=False, encoding='utf-8-sig')
df_inpatient_2.to_csv('/Users/hantswilliams/Dropbox/Biovirtua/Python_Projects/ahi/df_inpatient_2.csv', index=False, encoding='utf-8-sig')
df_outpatient_2.to_csv('/Users/hantswilliams/Dropbox/Biovirtua/Python_Projects/ahi/df_outpatient_2.csv', index=False, encoding='utf-8-sig')



########################################################################################################################
########################################################################################################################
########################################################################################################################









########################################################################################################################
########################################################################################################################
########################################################################################################################

### Want to compare 
# 	provider_id	hospital_name
#   	 330393	   SUNY/STONY BROOK UNIVERSITY HOSPITAL

# Create stonybrook datasets 
sb_hospital = df_hospital_2[df_hospital_2['provider_id'] == '330393']
sb_inpatient = df_inpatient_2[df_inpatient_2['provider_id'] == 330393]
sb_outpatient = df_outpatient_2[df_outpatient_2['provider_id'] == 330393]


sb_inpatient_analysis = sv.analyze(sb_inpatient)
sb_inpatient_analysis.show_html('/Users/hantswilliams/Dropbox/Biovirtua/Python_Projects/ahi/AHI_STATS_507/Week13_Summary/output/sweet_report_df_inpatient_sb.html')

sb_outpatient_analysis = sv.analyze(sb_outpatient)
sb_outpatient_analysis.show_html('/Users/hantswilliams/Dropbox/Biovirtua/Python_Projects/ahi/AHI_STATS_507/Week13_Summary/output/sweet_report_df_outpatient_sb.html')


########################################################################################################################
########################################################################################################################
########################################################################################################################


nonsb_hospital = df_hospital_2[df_hospital_2['provider_id'] != '330393']
nonsb_inpatient = df_inpatient_2[df_inpatient_2['provider_id'] != 330393]
nonsb_outpatient = df_outpatient_2[df_outpatient_2['provider_id'] != 330393]


my_report = sv.compare([sb_inpatient, "Inpatient_SB"], [nonsb_inpatient, "Inpatient_NonSB"])
my_report.show_html('/Users/hantswilliams/Dropbox/Biovirtua/Python_Projects/ahi/AHI_STATS_507/Week13_Summary/output/sweet_report_inpatient_compare.html')



















