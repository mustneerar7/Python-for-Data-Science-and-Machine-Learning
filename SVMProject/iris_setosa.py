import pandas as pd

# load data from iris dataset
from sklearn.datasets import load_iris

iris = load_iris()
dataframe = pd.DataFrame(iris['data'], columns=iris['feature_names'])
print(dataframe.head(3))

# classic train test split
from sklearn.model_selection import train_test_split

X = dataframe
y = iris['target']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=101
)

# using support vector machine model
from sklearn.svm import SVC

svm_model = SVC()
svm_model.fit(X_train, y_train)
predictions = svm_model.predict(X_test)

# printing results
from sklearn.metrics import confusion_matrix, classification_report

print(confusion_matrix(y_test, predictions))
print(classification_report(y_test, predictions))

# using grid search to find the best C and gamma
from sklearn.model_selection import GridSearchCV

param_grid = {
    'C':[0.1, 1, 10, 100, 1000], 
    'gamma': [1, 0.1, 0.01, 0.001, 0.0001]
}

# fitting the grid search model with training data
grid = GridSearchCV(SVC(), param_grid, verbose=3)
grid.fit(X_train, y_train)
print(grid.best_params_)

# printing results
print(confusion_matrix(y_test, grid.predict(X_test)))
print(classification_report(y_test, grid.predict(X_test)))
