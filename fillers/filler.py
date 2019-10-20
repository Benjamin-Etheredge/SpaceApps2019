import pandas as pd
from collections import defaultdict

class Filler:
    subclasses = []

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.subclasses.append(cls)

    @staticmethod
    def fill_column(data: pd.DataFrame, column_name: str) -> pd.DataFrame:
        raise NotImplementedError('Code it up you scrub!')
    @classmethod
    def main(self, data: pd.DataFrame, column_name: str):
        data = self.fill_column(data, column_name)
        assert(not data[column_name].isnull().any())
        return data
