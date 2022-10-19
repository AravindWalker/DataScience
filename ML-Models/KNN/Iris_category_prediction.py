# from sklearn import datasets
# from sklearn.model_selection import train_test_split
#
# iris = datasets.load_iris()
# X = iris.data
# y = iris.target
# print(X.shape)
# print(y.shape)
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
# print(X_train.shape)
# print(X_test.shape)
# print(y_train.shape)
# print(y_test.shape)
# print(iris)

import pandas as pd
from sklearn import neighbors, metrics
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

data = pd.read_csv(r"C:\Users\HP\OneDrive\Desktop\Data Science\SciKit_learn\car.data")
# print(data.head())
X = data[["buying", "maint", "safety"]].values
y = data["class"]
print(X)
# print(y)
le = LabelEncoder()
for i in range(len(X[0])):
    X[:, i] = le.fit_transform(X[:, i])
print(X)
# another method
label_mapping = {
    'unacc': 0,
    'acc': 1,
    'good': 2,
    'vgood': 3
}
y = y.map(label_mapping)
print(y)
# create model
knn_model = neighbors.KNeighborsClassifier(n_neighbors=25, weights="uniform")
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
knn_model.fit(X_train, y_train)
predictions = knn_model.predict(X_test)
accuracy = metrics.accuracy_score(y_test, predictions)
print("accuracy: ", accuracy)
print("predictions: ", predictions)
