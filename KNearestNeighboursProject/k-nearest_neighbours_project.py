import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

# read the unclassified data
df = pd.read_csv('KNN_Project_Data', index_col=0)
print(df.head())

# scale the data
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
scaler.fit(df.drop('TARGET CLASS', axis=1))
scaled_features = scaler.transform(df.drop('TARGET CLASS', axis=1))

# create dataframe from scaled data
df_scaled = pd.DataFrame(scaled_features, columns=df.columns[:-1])

# train test split
from sklearn.model_selection import train_test_split

X = df_scaled
y = df['TARGET CLASS']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)

# train KNeighbours model
from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(X_train, y_train)

# get predictions from model
pred = knn.predict(X_test)

from sklearn.metrics import classification_report, confusion_matrix

print(classification_report(y_test, pred))
print(confusion_matrix(y_test, pred))

# get a list of error values
error_values = []

for i in range(1, 40):
    knn = KNeighborsClassifier(n_neighbors=i)
    knn.fit(X_train, y_train)
    pred = knn.predict(X_test)

    error_values.append(np.mean(pred != y_test))

# create an error value chart (elbow method)
plt.figure(figsize = (10, 6))

plt.plot(
    range(1, 40),
    error_values, 
    color='blue', ls='--', 
    marker='o', markerfacecolor='red',
    markersize=10
)
plt.title("Error Rate vs K-Values")
plt.xlabel("K-Values")
plt.ylabel("Error Rate")

plt.show()

# choose a better K value (K=30)
knn = KNeighborsClassifier(n_neighbors=30)
knn.fit(X_train, y_train)

# get predictions
pred = knn.predict(X_test)

print(classification_report(y_test, pred))
print(confusion_matrix(y_test, pred))
