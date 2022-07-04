'''
Reference: https://medium.datadriveninvestor.com/k-fold-cross-validation-for-parameter-tuning-75b6cb3214f

- How k-fold cross validation helps in tuning the parameters of a model (here, the model is a k-nearest neighbors)
- k-fold cross-validation is a technique used to evaluate the performance of a model by dividing the dataset into k subsets,
    each of which is used once as a test set and the remaining k-1 subsets are used as training sets.


'''
# Tested on iris dataset

# load libraries
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn import datasets

# load dataset
iris = datasets.load_iris()

# Since this is a bunch, create a dataframe
iris_df = pd.DataFrame(iris.data)
iris_df['class'] = iris.target

iris_df.columns = ['sepal_len', 'sepal_wid', 'petal_len', 'petal_wid', 'class']
iris_df.dropna(how="all", inplace=True)  # remove any empty lines

# selecting only first 4 columns as they are the independent(X) variable
# any kind of feature selection or correlation analysis should be first done on these
iris_X = iris_df.iloc[:, [0, 1, 2, 3]]
iris_y = iris_df.iloc[:, 4]

X = iris_X
y = iris_y

# splitting into train and test data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3)

# fitting k-nearest neighbours algorithm
knn1 = KNeighborsClassifier(n_neighbors=3)
knn1.fit(X_train, y_train)
y_pred = knn1.predict(X_test)

# calculating accuracy
print('Acuuracy score is {}'.format(accuracy_score(y_test, y_pred)))


# hyper parameter tuning.
# Selecting best K
neighbors = [x for x in range(1, 50) if x % 2 != 0]

# empty list that will hold cv scores
cv_scores = []
for k in neighbors:
    knn = KNeighborsClassifier(n_neighbors=k)
    scores = cross_val_score(knn, X, y, cv=10, scoring='accuracy')
    cv_scores.append(scores.mean())  # graphical view

# misclassification error
MSE = [1-x for x in cv_scores]

# optimal K
optimal_k_index = MSE.index(min(MSE))
optimal_k = neighbors[optimal_k_index]
print(optimal_k)

# plot misclassification error vs k
plt.plot(neighbors, MSE)
plt.xlabel('Number of Neighbors K')
plt.ylabel('Misclassification Error')
plt.show()
