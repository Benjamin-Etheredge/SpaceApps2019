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
```

```python
X.head()
```

```python
y.head()
```
