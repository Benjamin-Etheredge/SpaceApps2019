import Filler
from HelperTestingFunctions import get_testing_dataset

import pandas as pd

from copy import deepcopy
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.linear_model import LinearRegression


class Handler:
    def __init__(self):
        pass

    # TODO Finish method to return list of all functions
    @staticmethod
    def get_filler_methods() -> list:
        # print(Filler.Filler.__subclasses__())
        return []

    # TODO return all column names that are missing values
    @staticmethod
    def get_columns_with_missing_values(data: pd.DataFrame) -> list:
        return data.columns[data.isnull().any()]

    @staticmethod
    def temp():
        return 'a', 'b'

    @staticmethod
    def classifier(values):
        pass

    # TODO Finish method to return best fill method
    @staticmethod
    def find_best_fill_method(data: pd.DataFrame, label: str) -> pd.DataFrame:
        filler_methods = Handler.get_filler_methods()
        columns_with_missing_values = Handler.get_columns_with_missing_values(data)

        y = data[label]
        x = data.drop(labels=[label], axis=1)
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=4)

        values = {column: filler_methods for column in columns_with_missing_values}
        regressor = LinearRegression()

        grid_acc = GridSearchCV(regressor, param_grid=values, scoring='explained_variance')
        grid_acc.fit(x_train, y_train)
        return data

        #= hp.choice("filler", []


def classifier_builder(values):
    pass


if __name__ == "__main__":
    test_df, label = get_testing_dataset()
    result = Handler.find_best_fill_method(test_df, label)
    print("WE RAN YALL")
    print(result.describe())


