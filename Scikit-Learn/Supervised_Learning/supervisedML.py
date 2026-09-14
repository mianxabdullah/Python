#Linear Regression
from sklearn.linear_model import LinearRegression
X=[[1],[2],[3],[4],[5]] #hour studied
y=[10,20,30,40,50] # marks obtained
model=LinearRegression()
model.fit(X,y)
hourss=float(input("Enter hours studied : "))
want_to_prdict=[[hourss]]
y_pred=model.predict(want_to_prdict)
print("Predicted values :\n",y_pred)

#Logistic Regression is a classification algorithm
from sklearn.linear_model import LogisticRegression
X=[[1],[2],[3],[4],[5]] # hours studied
y=[0,0,1,1,1] # pass or fail (0 or 1)
model=LogisticRegression()
model.fit(X,y)  
hours=float(input("Enter hours studied : "))
want_to_predict=[[hours]]       
y_pred=model.predict(want_to_predict)
if y_pred[0]==0:
    print("Fail")           
else:
    print("Pass")   

#KNN is a classification algorithm that classifies a data point based on the majority class of its k nearest neighbors in the feature space. It is a non-parametric algorithm that does not make any assumptions about the underlying data distribution and it is used for both classification and regression problems. It is sensitive to the choice of k and the distance metric used to calculate the distance between data points.
from sklearn.neighbors import KNeighborsClassifier
X=[[180,7],[160,6],[170,8],[150,5],[190,9]] # weight and size
y=[0,0,1,1,1] # 0 for apple and 1 for orange
model=KNeighborsClassifier(n_neighbors=3)# take k as odd number to avoid tie
model.fit(X,y)
height=float(input("Enter weight : "))
weight=float(input("Enter size : "))
want_to_predict=[[height,weight]]
y_pred=model.predict(want_to_predict)
if y_pred[0]==0:
    print("Apple")
else:
    print("Orange")

#decision tree is a classification algorithm that uses a tree-like model of decisions and their possible consequences. It is a non-parametric algorithm that does not make any assumptions about the underlying data distribution and it is used for both classification and regression problems. It is sensitive to the choice of features and the depth of the tree.
from sklearn.tree import DecisionTreeClassifier
X=[[180,7],[160,6],[170,8],[150,5],[190,9]] # weight and size
y=[0,0,1,1,1] # 0 for apple and 1 for orange
model=DecisionTreeClassifier()  
model.fit(X,y)  
height=float(input("Enter weight : "))
weight=float(input("Enter size : "))
want_to_predict=[[height,weight]]
y_pred=model.predict(want_to_predict)
if y_pred[0]==0:
    print("Apple")
else:
    print("Orange") 

    