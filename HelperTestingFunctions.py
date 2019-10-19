# TODO implement method to get a dataset from sclearn for testing
def get_testing_dataset():
    import pandas as pd
    from sklearn.datasets import fetch_california_housing
    cal_housing = fetch_california_housing()
    X, y = cal_housing.data, cal_housing.target
    names = cal_housing.feature_names
    X = pd.DataFrame(X, columns=names)
    y = pd.Series(y)
    data = X
    data["target"] = y
    return data, "target"
