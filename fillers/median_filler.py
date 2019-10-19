import Filler


class MedianFiller(Filler.Filler):
    def fill_column(data: pd.DataFrame, column_name: str) -> pd.DataFrame:
        data[column_name] = data[column_name].fillna(data[column_name].median())
        return data