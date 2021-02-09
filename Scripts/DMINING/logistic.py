from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegressionCV


cancer = load_breast_cancer()


X = cancer.data
Y = cancer.target

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=33)

print(X_train)
print(Y_train)

model = LogisticRegressionCV(max_iter=50000)
model.fit(X_train,Y_train)
# print(model.score(X_test,Y_test))

y_pre = model.predict_proba(X_train)
print(y_pre)
