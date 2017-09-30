from sklearn import datasets,metrics
from sklearn.naive_bayes import GaussianNB
from sklearn.cross_validation import train_test_split
d=datasets.load_iris()
x=d.data
y=d.target
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.7)
model=GaussianNB()
model.fit(x_train,y_train)
Y=model.predict(x_test)
print(metrics.accuracy_score(y_test,Y))