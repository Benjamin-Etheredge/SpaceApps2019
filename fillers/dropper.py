from sklearn.preprocessing import Imputer
import numpy as np
from fillers import Filler
import pandas as pd


class Filler_Dropper(Filler):
    @staticmethod
    def fill_column(data: pd.DataFrame, column_name: str) -> pd.DataFrame:
        data[column_name] = data[column_name].fillna(data[column_name].mode()[0])

        return data
        data = data.dropna(subset=[column_name], how='any')
        return data
