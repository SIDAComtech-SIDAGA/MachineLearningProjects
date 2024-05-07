#MOST COMMON TASKS IN MACHINE LEARNING IS
# 1. CLASSIFICATION TASKS which deals with categorical data (descrete variables)
# 2. REGRESSION TASKS which deals most with continuous varaibles such as prediction predicting houses prices
#
#BUT ALSO THERE ARE OTHERS AS FOOLOWS
# CLUSTERING
#DIMENSIONALITY REDUCTION
# ANOMARY DETECTION
# ASSOCIATION RULE LEARNING
# RECCOMENDATION SYSTEM
# TIME SERIES FORECASTING


#LINEAR REGRESSION ALGROTHIM
# CODE 
from sklearn.linear_model import LinearRegression
model =  LinearRegression()
model.fit(X_train, y_train)

#DECISION TREE ALGORTHIM

from sklearn.tree import DecisionTreeClassifier
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

#SUPPORT VECTOR MACHINE LEARNING
from sklearn.svm import SVC
model = SVC()
model.fit(X_train, y_train)

#NAIVE BAYES ALGORITHM 

from sklearn.naive_bayes import GaussianNB
model = GaussianNB()
model.fit(X_train, y_train)

#LOGISTIC REGRESSION

from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
model.fit(X_train, y_train)

#RANDOM FOREST Is the type of esseble learning method based on multiple desicion trees to improve
#prediction accuracy
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier()
model.fit(X_train, y_train)

#K-NEAREST NEIGHBORS(KNN)

from sklearn.neighbors import KNeighborsClassifier
model = KNeighborsClassifier()
model.fit(X_train, y_train)

#GRADIENT BOOSTING MACHINES(GBMS)
from sklearn.ensemble import GradientBoostingClassifier
model = GradientBoostingClassifier()
model.fit(X_train, y_train)
