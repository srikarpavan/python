import numpy as np
#import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn import metrics
from sklearn.model_selection import train_test_split

iris = datasets.load_iris()         # Loading Iris datasets from the given source


from sklearn.svm import SVC

X = iris.data
y = iris.target
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

svm = SVC()                        # Fitting SVM model to the data
expected = iris.target

# Training the Model on Testing Set

svm.fit(X_train, y_train)
print(expected)

predicted_label = svm.predict(iris.data)          # Making Prediction based on X, Y
print(predicted_label)

# Cross Validation compare the predicted and expected values
# Matrix which is used to find the accuracy of classification
print(metrics.confusion_matrix(expected, predicted_label))

# Cross Validation compare the predicted and expected values
print(metrics.classification_report(expected, predicted_label))

print('Accuracy of SVM classifier on training set: {:.2f}'
     .format(svm.score(X_train, y_train)))
# Evaluating the Model based on Testing Part
print('Accuracy of SVM classifier on test set: {:.2f}'
     .format(svm.score(X_test, y_test)))