"""Sample code from Siraj class"""
from sklearn import tree

# [height, weight, shoe size]
X = [[181, 80, 33],
     [177, 70, 43],
     [160, 60, 38],
     [154, 54, 32],
     [166, 65, 40],
     [190, 90, 47],
     [175, 64, 39],
     [177, 70, 40],
     [152, 60, 36],
     [171, 75, 42],
     [181, 85, 43]]

Y = ['male', 'female', 'female', 'female', 'male', 'male',
     'male', 'female', 'male', 'female', 'male']

clf = tree.DecisionTreeClassifier()

clf = clf.fit(X, Y)

prediction = clf.predict([[190, 70, 43]])

print(prediction)
