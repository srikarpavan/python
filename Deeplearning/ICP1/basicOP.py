import pandas
# import tensorflow as tf
from keras.models import Sequential
from keras.layers.core import Dense, Activation

# load dataset
from nltk import pr
from sklearn.model_selection import train_test_split
import pandas as pd
dataset = pd.read_csv("C:/Users/pavan/Downloads/Python_Lesson5/Python_Lesson5/diabetes.csv", header=None).values
# print(dataset)
import numpy as np
X_train, X_test, Y_train, Y_test = train_test_split(dataset[:,0:8], dataset[:,8],
                                                    test_size=0.25, random_state=87)
np.random.seed(155)
my_first_nn = Sequential() # create model
my_first_nn.add(Dense(20, input_dim=8, activation='relu'))# hidden layer
my_first_nn.add(Dense(142, activation='sigmoid'))
my_first_nn.add(Dense(156, activation='softmax')) #added one laye
my_first_nn.add(Dense(7, activation='softplus')) #added another layer
my_first_nn.add(Dense(1, activation='sigmoid')) # output layer
my_first_nn.compile(loss='binary_crossentropy', optimizer='adam')
my_first_nn_fitted = my_first_nn.fit(X_train, Y_train, epochs=100, verbose=0,
                                     initial_epoch=0)
print(my_first_nn.summary())
print(my_first_nn.evaluate(X_test, Y_test, verbose=0) *100)