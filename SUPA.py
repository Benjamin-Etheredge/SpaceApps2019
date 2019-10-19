import Filler
from HelperTestingFunction import get_testing_dataset

import pandas as pd


class Handler:
    def __init__(self):
        pass

    # TODO Finish method to return list of all functions
    @staticmethod
    def get_filler_methods() -> list:
        # print(Filler.Filler.__subclasses__())
        return []

    # TODO FInish method to return best fill method
    # Requres get_filler_methods
    @staticmethod
    def find_best_fill_method(data: pd.DataFrame, label: str):
        filler_methods = self.get_filler_methods()




if __name__ == "__main__":
    handler = Handler()
    handler.get_filler_methods()
