import pandas as pd

data = pd.read_csv(r"iris.data", header=None)

data[4] = data[4].replace("Iris-setosa", "1")
data[4] = data[4].replace("Iris-versicolor", "2")
data[4] = data[4].replace("Iris-virginica", "3")

data_shuffled = data.sample(frac=1)  # shuffle
