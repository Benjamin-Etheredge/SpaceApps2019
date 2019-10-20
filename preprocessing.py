# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 10:58:03 2019

@author: hgandiko
"""

import pandas as pd
import numpy as np

def preprocessing(df, display_stats=True):
    df.replace('', np.nan, inplace = True)
    df.replace(np.nan, 'None', inplace = True)
    col_uniqueval = {}

    for col in df.columns:
        col_uniqueval[col] = df[col].nunique()
    
    for item in col_uniqueval:
        if(col_uniqueval[item] == 1):
            df.drop([item],axis=1, inpace =True)
            
    col_dtypedict = {}

    for col in df.columns:
        col_dtypedict[col] = df[col].dtypes
    
    prior_totalmemoryusage = 0
    if(display_stats):
        print("PRIOR:")
        print(df.info(memory_usage='deep'))
        prior_totalmemoryusage = df.memory_usage(index=True).sum()
        print("OVERALL MEMORY USAGE: ", prior_totalmemoryusage)

    for item in col_dtypedict:
        if(col_dtypedict[item] == 'int64'):
            df[item]=df[item].astype('int32')
        elif(col_dtypedict[item] == 'float64'):
            df[item]=df[item].astype('float32')
    
    post_totalmemoryusage = 0
    if(display_stats):
        print("POST:")
        print(df.info(memory_usage='deep'))
        post_totalmemoryusage = df.memory_usage(index=True).sum()
        print("OVERALL MEMORY USAGE: ", post_totalmemoryusage)
        
    if(display_stats):
        print("OVERALL MEMORY USAGE IMPROVEMENT: ", get_change(post_totalmemoryusage, prior_totalmemoryusage))
            
    return df