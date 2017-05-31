from sklearn import tree
from sklearn import svm
from sklearn import neighbors
from sklearn import discriminant_analysis
from sklearn import linear_model


dt = tree.DecisionTreeClassifier()

# CHALLENGE - create 3 more classifiers...
# 1
lsvc = svm.LinearSVC()

# 2
kn = neighbors.KNeighborsClassifier(3)

# 3
svc = svm.SVC()

classifiers = [ dt, lsvc, kn, svc ]

# [height, weight, shoe_size]
X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40],
     [190, 90, 47], [175, 64, 39],
     [177, 70, 40], [159, 55, 37], [171, 75, 42], [181, 85, 43]]

male = 'male'
female = 'female'

Y = [male, male, female, female, male, male, female, female,
     female, male, male]

# CHALLENGE - ...and train them on our data
for clf in classifiers:
    clf = clf.fit(X, Y)
    prediction = clf.predict([[190, 70, 43]])
    print("%s %s" % (clf, prediction))


# CHALLENGE compare their results and print the best one!