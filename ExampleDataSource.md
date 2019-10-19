---
jupyter:
  jupytext:
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.1'
      jupytext_version: 1.2.1
  kernelspec:
    display_name: SpaceApps
    language: python
    name: spaceapps
---

Loads an exmple Data set for testing. 

```python
import pandas as pd
from sklearn.datasets import fetch_california_housing
cal_housing = fetch_california_housing()
X, y = cal_housing.data, cal_housing.target
names = cal_housing.feature_names
X = pd.DataFrame(X, columns=names)
y = pd.Series(y)
data = X
data["target"] = y

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
missing_data = make_missing_data(data, n=.25)
```

```python
X.head()
```

```python
y.head()
```

```python
data.head()
```

```python

```

```python

```
