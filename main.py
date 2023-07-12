import pandas as pd

data = pd.read_csv(r"iris.data",)

data.loc[data['species'] == 'Iris-setosa', 'species'] = 'apple'
data.loc[data['species'] == 'Iris-versicolor', 'species'] = 'cherry'
data.loc[data['species'] == 'Iris-virginica', 'species'] = 'blueberry'