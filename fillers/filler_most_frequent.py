# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 18:01:52 2019

@author: hgandiko
"""

from sklearn.preprocessing import Imputer
import numpy as np
from fillers import Filler
import pandas as pd


class Filler_MostFrequent(Filler):
    @staticmethod

    def fill_column(data: pd.DataFrame, column_name: str) -> pd.DataFrame:

        data[column_name] = data[column_name].fillna(data[column_name].mode()[0])
        assert(data[column_name].isnull().sum() == 0)
        return data
        #Jdata[column_name] = data[column_name].fillna(data[column_name].mode())
        #return data

        allowable_datatypes = ['float64','int64', 'float32','int32', 'string32','string64', 'O']
        imputer = Imputer(missing_values='NaN', strategy='most_frequent')

        if(data[column_name].dtype in allowable_datatypes):
            imputer.fit(data[column_name].values.reshape(-1, 1))
            data[column_name]= imputer.transform(data[column_name].values.reshape(-1, 1))
        else:
            raise

        return data
