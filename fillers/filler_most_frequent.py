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
