# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 18:01:52 2019

@author: hgandiko
"""

from sklearn.preprocessing import Imputer
import numpy as np
import Filler

class Filler_MostFrequent(Filler):
    @staticmethod
    allowable_datatypes = ['float64','int64', 'float32','int32', 'string32','string64', 'O']
    def fill_column(data: pd.DataFrame, column_name: str) -> pd.DataFrame:
        imputer = Imputer(missing_values='NaN', strategy='most_frequent')
        
        if(df[column_name].dtype in allowable_datatypes):
            imputer.fit(data[column_name].values.reshape(-1, 1))
            data[column_name]= imputer.transform(data[column_name].values.reshape(-1, 1))
        else:
            raise
        
        return data