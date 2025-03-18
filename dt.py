import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
cl={'mediumturquoise','lightcoral','lightpink'}
df=pd.read_csv("D:\College\penguins_size.csv")
df=df.dropna()
print(df.head())
plt.subplots(figsize=(8,8))
df_2dhist = pd.DataFrame({
    x_label: grp['island'].value_counts()
    for x_label, grp in df.groupby('species')
})
sns.heatmap(df_2dhist, cmap='viridis')
plt.show()
plt.xlabel('Species')
_ = plt.ylabel('Island')
df.groupby('species').size().plot(kind='barh',color=cl)
plt.gca().spines[['top', 'right',]].set_visible(False)
plt.show()
sns.scatterplot(x='culmen_length_mm',y='culmen_depth_mm',data=df,hue='species',palette=cl)
plt.show()
sns.catplot(x='species',y='culmen_length_mm',data=df,kind='box',col='sex',palette=cl)
plt.show()
print(pd.get_dummies(df))
X = pd.get_dummies(df.drop('species',axis=1),drop_first=True)
y = df['species']
print(X.shape)
print(y.shape)
print(X.head())
print(y.head())
print(y.unique())
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3, random_state=42)
from sklearn.tree import DecisionTreeClassifier
model = DecisionTreeClassifier(criterion='entropy')
model.fit(X_train, y_train)
from sklearn.tree import plot_tree
plt.figure()
plot_tree(model);
plt.show()
plt.figure(figsize=(15,15),dpi=150)
plot_tree(model,filled=True,feature_names=X.columns);
plt.show()
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
sns.boxplot(x='species',y='body_mass_g',data=df)
plt.show()
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
penguin_model = 'decision_tree_model.pkl'  # Choose a filename
pickle.dump(pruned_tree, open(penguin_model, 'wb'))
loaded_model = pickle.load(open('decision_tree_model.pkl', 'rb'))
row_200 = X.iloc[200]
print(row_200)
new_data =[[33,11,183,3773,1.0,0.0,1.0,0.0]]
prediction = loaded_model.predict(new_data)
print(prediction)
