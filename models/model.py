from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from joblib import dump,load

iris = datasets.load_iris()

X_train,X_test,y_train,y_test = train_test_split(iris['data'],iris['target'],test_size=0.2,random_state=2019)

# training the model 
clf = RandomForestClassifier()
clf.fit(X_train,y_train)

predicted_values = clf.predict(X_test)

accuracy = accuracy_score(y_test,predicted_values)
print(predicted_values)
print(accuracy)
# Save the model as a pickle in a file
# dump(clf, 'iris_rf.pkl')