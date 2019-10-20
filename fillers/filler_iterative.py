from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
import numpy as np
from fillers import Filler
import pandas as pd


class Filler_Iterative(Filler):
    @staticmethod

    def fill_column(data: pd.DataFrame, column_name: str) -> pd.DataFrame:
        imp = IterativeImputer(max_iter=10, random_state=0)
        imp_data = pd.DataFrame(imp.fit_transform(data), columns = data.columns)
        data[column_name] = imp_data[column_name]
        return data
