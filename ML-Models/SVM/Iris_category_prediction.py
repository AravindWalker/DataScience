from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn import metrics

iris = datasets.load_iris()
X = iris.data
y = iris.target
print(X.shape)
print(y.shape)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
classes = iris.target_names
svm_model = svm.SVC()
svm_model.fit(X_train, y_train)
predictions = svm_model.predict(X_test)
accuracy = metrics.accuracy_score(y_test, predictions)
print("accuracy: ", accuracy)
print("predictions: ", predictions)
for i, j in enumerate(predictions):
    print(classes[j], end=" ")
