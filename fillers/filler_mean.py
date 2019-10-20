# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 18:01:06 2019

@author: hgandiko
"""

from sklearn.preprocessing import Imputer
import numpy as np
from fillers import Filler
import pandas as pd

class Filler_Mean(Filler):

    @staticmethod
    def fill_column(data: pd.DataFrame, column_name: str) -> pd.DataFrame:
        data[column_name] = data[column_name].fillna(data[column_name].mean())
        return data
