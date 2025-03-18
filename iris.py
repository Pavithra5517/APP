import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv("D:\College\iris.csv")
df=df.dropna()
df.head()
df=df.drop('Id', axis=1)
X = pd.get_dummies(df.drop('Species',axis=1),drop_first=True)
y = df['Species']
print(X.shape)
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3, random_state=42)
from sklearn.tree import DecisionTreeClassifier
model = DecisionTreeClassifier(criterion='entropy')
model.fit(X_train, y_train)
from sklearn.tree import plot_tree
plt.figure()
base_pred = model.predict(X_test)
from sklearn.metrics import confusion_matrix,classification_report, ConfusionMatrixDisplay
cm = confusion_matrix(y_test,base_pred)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=model.classes_)
disp.plot()
plt.show()
base_report = classification_report(y_test,base_pred)
print(base_report)
model.feature_importances_
print(pd.DataFrame(index=X.columns,data=model.feature_importances_,columns=['Feature Importance']))
def report_model(model):
    model_preds = model.predict(X_test)
    print(classification_report(y_test,model_preds))
    print('\n')
    plt.figure(figsize=(12,8),dpi=150)
    plot_tree(model,filled=True,feature_names=X.columns);
pruned_tree = DecisionTreeClassifier(criterion='entropy',max_depth=2)
pruned_tree.fit(X_train,y_train)
report_model(pruned_tree)
plt.show()
import pickle

# Assuming you already have your trained model 'pruned_tree'
penguin_model = 'decision_tree_iris.pkl'  # Choose a filename
pickle.dump(pruned_tree, open(penguin_model, 'wb'))
loaded_model = pickle.load(open('decision_tree_iris.pkl', 'rb'))
row_10 = X.iloc[10]
print(row_10)
new_data =[[4.5,3.5,1.5,0.2]]
prediction = loaded_model.predict(new_data)
print(prediction)
