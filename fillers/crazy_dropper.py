from sklearn.preprocessing import Imputer
import numpy as np
from fillers import Filler
import pandas as pd


class Filler_Crazy_Dropper(Filler):
    @staticmethod
    def fill_column(data: pd.DataFrame, column_name: str) -> pd.DataFrame:
        #data[column_name] = data[column_name].fillna(data[column_name].mode()[0])
        #return data
        #import copy
        #new_data = copy.deepcopy(data)
        new_data = data.dropna(how='any')
        #new_data.isnull().sum()
        assert(data[column_name].isnull().any())
        return new_data
