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
    missing_data = make_missing_data(data, n=.25)
    return missing_data, "target"

def get_testing_dataset_vanilla():
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


def random_missing_ix(data, n=.25, random_state=811):
    if n < 1.0:
        n = int(n * data.shape[0])

    return data.sample(n=n, random_state=random_state).index


def make_missing_data(data, n=.25):
    random_seed = 1
    for col in data.columns:
        missing_data_ix = random_missing_ix(data, n=n, random_state=random_seed)
        data[col].iloc[missing_data_ix] = None
        random_seed += 1
    return data


