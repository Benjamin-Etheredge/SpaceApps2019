from collections import OrderedDict

import Filler
from HelperTestingFunctions import get_testing_dataset

import pandas as pd

from hyperopt import hp
from hyperopt import fmin, tpe
from copy import deepcopy
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score


def fill_column(data: pd.DataFrame, column_name: str) -> pd.DataFrame:
    data[column_name] = data[column_name].fillna(data[column_name].median())
    return data

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
        #filler_methods = [fill_column]
        columns_with_missing_values = Handler.get_columns_with_missing_values(data)


        if len(columns_with_missing_values) == 0:
            return data

        print(data.info())

        values = {column: filler_methods for column in columns_with_missing_values}

        names_methods = [(column_name, filler_methods) for column_name in columns_with_missing_values]
        print(f"names_methods: {names_methods}")
        space = {column_name: hp.choice(column_name, filler_methods) for column_name in columns_with_missing_values}
        print(f"space: {space}")
        #trails =fill_column
        from hyperopt import Trials
        # Create a trials object
        tpe_trials = Trials()

        import random
        def objective(args):
            print("objective---------------------")
            print(f"args: {args}")
            new_data = deepcopy(data)

            try:
                for column in args.keys():
                    new_data = args[column](new_data, column)
            except:
                # TODO imporve
                return 999999

            y = new_data[label]
            x = new_data.drop(labels=[label], axis=1)

            model = LinearRegression()

            score = cross_val_score(model, x, y, cv=5, scoring='explained_variance')
            return 1/(sum(score)/len(score))

        best = fmin(fn=objective, space=space, algo=tpe.suggest, trials=tpe_trials, max_evals=100)
        print(best)
        return data

        #= hp.choice("filler", []


def classifier_builder(values):
    pass

def space(column_names, functions):
    return space




if __name__ == "__main__":
    test_df, label = get_testing_dataset()
    #print(test_df.isnull().sum())
    result = Handler.find_best_fill_method(test_df, label)
    print("WE RAN YALL")
    print(result.describe())


