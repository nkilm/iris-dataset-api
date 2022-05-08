from sklearn import datasets
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from joblib import dump

iris = datasets.load_iris()

X_train,X_test,y_train,y_test = train_test_split(iris['data'],iris['target'],test_size=0.2,random_state=2019)

# training the model 
clf = LogisticRegression(solver='lbfgs', max_iter=1000)
clf.fit(X_train,y_train)

predicted_values = clf.predict(X_test)

accuracy = accuracy_score(y_test,predicted_values)

# Save the model as a pickle in a file
dump(clf, 'iris_lr.pkl')