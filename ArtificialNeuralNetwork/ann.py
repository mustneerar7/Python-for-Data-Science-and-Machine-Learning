import numpy as np
import pandas as pd

# step 1 - data preprocessing

# import data from file
dataset = pd.read_csv('Churn_Modelling.csv')

# remove unnecessary columns
# create X and y sets
X = dataset.iloc[:, 3:13].values
y = dataset.iloc[:, 13].values

# transcode columns with string data to float
from sklearn.preprocessing import LabelEncoder

le_X_1 = LabelEncoder()
X[:, 1] = le_X_1.fit_transform(X[:, 1])

le_X_2 = LabelEncoder()
X[:, 2] = le_X_2.fit_transform(X[:, 2])

# transcode float data with more than binary outcomes
from sklearn.preprocessing import OneHotEncoder

oneHotEncoder = OneHotEncoder()
oneHotEncoder.fit_transform(X).toarray()

X = X[:, 1:]

# prepare test and training datasets
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=0)

# scale data evenly using standard scaler
from sklearn.preprocessing import StandardScaler

sc = StandardScaler()

X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# step 2 - creating an artificial neural network

import tensorflow as tf

# importing tf Sequential model
ann = tf.keras.models.Sequential()

# adding first input + hidden layer
ann.add(tf.keras.layers.Dense(6, activation='relu'))
# adding second hidden layer
ann.add(tf.keras.layers.Dense(6, activation='relu'))
# adding the output layer
ann.add(tf.keras.layers.Dense(1, activation='sigmoid'))

# compiling ann
ann.compile(
    optimizer='adam', loss= 'binary_crossentropy', metrics=['accuracy']
)

# fitting the data
ann.fit(X_train, y_train, batch_size=10, epochs=100)

# 3 - getting results from ann

# getting predictions
y_pred = ann.predict(X_test)
y_pred = (y_pred > 0.5)

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
