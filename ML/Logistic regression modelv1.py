import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
df = pd.read_csv("https://github.com/thechibuzor1/machine-learning/blob/main/ML/titanic.csv")
df['Male'] = df['Sex'] == 'Male'
X = df[['Pclass','Male','Age','Siblings/Spouses','Parents/Children','Fare']].values
y = df['Survived'].values

X_train,X_test,y_train,y_test = train_test_split(X,y)

model = DecisionTreeClassifier()
model.fit(X_train,y_train)

y_pred = model.predict(X_test)


print("Model score: ", model.score(X_test,y_test))
