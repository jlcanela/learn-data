from sklearn import tree
from sklearn import neighbors
from sklearn import discriminant_analysis
from sklearn import linear_model
from sklearn import svm

clf = tree.DecisionTreeClassifier()

# CHALLENGE - create 3 more classifiers...
# 1
kn = neighbors.KNeighborsClassifier(3)

# 2
lin = discriminant_analysis.LinearDiscriminantAnalysis()

# 3
quad = discriminant_analysis.QuadraticDiscriminantAnalysis()

# 4
svc = svm.SVC()

# [height, weight, shoe_size]
X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40],
     [190, 90, 47], [175, 64, 39],
     [177, 70, 40], [159, 55, 37], [171, 75, 42], [181, 85, 43]]

male = 'male'
female = 'female'

Y = [male, male, female, female, male, male, female, female,
     female, male, male]

# CHALLENGE - ...and train them on our data
clf = clf.fit(X, Y)
prediction = clf.predict([[190, 70, 43]])

# CHALLENGE compare their reusults and print the best one!

print(prediction)

kn = kn.fit(X, Y)
prediction1 = kn.predict([[190, 70, 43]])
print(prediction1)

lin = lin.fit(X, Y)
prediction2 = lin.predict([[190, 70, 43]])
print(prediction2)

quad = quad.fit(X, Y)
prediction3 = quad.predict([[190, 70, 43]])
print(prediction3)

svc = svc.fit(X, Y)
prediction4 = svc.predict([[190, 70, 43]])
print(prediction4)
