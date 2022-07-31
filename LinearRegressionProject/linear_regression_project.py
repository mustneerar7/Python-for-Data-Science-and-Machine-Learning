import numpy as np
import pandas as pd

# Read in the Ecommerce Customers csv file 
# as a DataFrame called customers
customers = pd.read_csv('Ecommerce Customers')

# Check the head of customers, 
# and check out its info() and describe() methods
customers.head()
customers.describe()
customers.info()

# Set a variable X equal to the numerical features 
# of the customers and a variable y equal to 
# the "Yearly Amount Spent" column.
X = customers[
       ['Avg. Session Length', 'Time on App',
       'Time on Website', 'Length of Membership']
]

y = customers['Yearly Amount Spent']

# Use model_selection.train_test_split from sklearn to
# split the data into training and testing sets. 
# Set test_size=0.3 and random_state=101
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
       X, y, test_size=0.3, random_state=101
)

# Import LinearRegression from sklearn.linear_model
# Create an instance of a LinearRegression() model
from sklearn.linear_model import LinearRegression
model = LinearRegression(
       copy_X=True, fit_intercept=True, 
       n_jobs=1, normalize=False
)

# Train/fit lm on the training data
model.fit(X_train, y_train)

# Print out the coefficients of the model
print(model.coef_)
cdf = pd.DataFrame(model.coef_, X.columns, columns=['Coeff'])
print(cdf)

# Use predict() to predict off the X_test set of the data.
predictions = model.predict(X_test)
print(predictions)

# Create a scatterplot of the real test values 
# versus the predicted values
import matplotlib.pyplot as plt
plt.scatter(y_test, predictions)
plt.show()

# Calculate the Mean Absolute Error, Mean Squared Error, 
# and the Root Mean Squared Error. 
# Refer to the lecture or to Wikipedia for the formulas
from sklearn import metrics
mean_abs_error =  metrics.mean_absolute_error(y_test, predictions)
mean_sq_error = metrics.mean_squared_error(y_test, predictions)
root_mean_sq_error = np.sqrt(
       metrics.mean_squared_error(y_test, predictions)
)

print(mean_abs_error)
print(mean_sq_error)
print(root_mean_sq_error)

# Plot a histogram of the residuals and 
# make sure it looks normally distributed.
# Use either seaborn distplot, or just plt.hist()
import seaborn as sbn
sbn.displot((y_test - predictions))

plt.show()

# SOME PARTS INVOLVING USE OF SEABORN WERE
# NOT COMPLETED AS SKIPPED IN SELECTED TOPICS.
