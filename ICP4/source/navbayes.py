from sklearn import datasets
from sklearn.naive_bayes import GaussianNB
from matplotlib import pyplot as plot
from sklearn import metrics
from sklearn.model_selection import train_test_split

iris = datasets.load_iris()   # Loading Iris datasets


model = GaussianNB()      # Fitting gaussian Naive Bayes model to the data
model.fit(iris.data, iris.target)

expected = iris.target            # Making Prediction based on X, Y
predicted = model.predict(iris.data)

# Matplotlib
plot.plot(expected, predicted)     # graph for expected and predicted
print(expected)
print(predicted)
plot.show()

print(metrics.classification_report(expected, predicted))    #Cross Validation compare the predicted and expected values

print(metrics.confusion_matrix(expected, predicted))         # Matrix which is used to find the accuracy of classification
X_train, X_test, Y_train, Y_test = train_test_split(iris.data, iris.target, test_size=0.2, random_state=0)

model.fit(X_train, Y_train)                                  #  Model on Training Set

Y_predicted = model.predict(X_test)                           #  Model on Testing Set

print("accuracy using Gaussian Model is ", metrics.accuracy_score(Y_test, Y_predicted) * 100)
