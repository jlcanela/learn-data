# Learn data science and machine learning

## Learn Python for Data science #1

Code:

* [Github source code](https://github.com/jlcanela/learn-data/tree/master/learn-python-for-data-science-1)

Videos:

* [Learn Python for Data science #1](https://www.youtube.com/watch?v=T5pRlIbr6gg)

Documentation:

* [Scikit documentation](http://scikit-learn.org/stable/user_guide.html) to find alternate models
* [Docstring conventions](https://www.python.org/dev/peps/pep-0257/) helpfull to fix pylint errors

What did I learn ?

* Siraj's videos are awesome :)))), @Siraj, when you come to Paris ping me and let's have a drink, you rock !
* Thanks to some tipos in buggy.py, I discovered that when data are incoherent, DecisionTreeClassifier.predict is returning sometimes 'male', sometimes 'female'
  * caused by mismatch in both X and Y values
  * DecisionTreeClassifier is using [numpy.random.RandomState](https://docs.scipy.org/doc/numpy/reference/generated/numpy.random.RandomState.html) according to [doc](http://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html) 
  * It's *really* *important* to **always** test the model and not starting to code without checking the data manually
* About testing
  * [unittest](https://docs.python.org/3/library/unittest.html) is fine to start with
  * Python ecosystem have [a lot](https://wiki.python.org/moin/PythonTestingToolsTaxonomy) of testing tools
  * I'll probably use [behave](https://pypi.python.org/pypi/behave), a BDD style library, later
* About scikit
  * [doc](http://scikit-learn.org/stable/documentation.html) looks very good
  * even found a [classifier comparaison page](http://scikit-learn.org/stable/auto_examples/classification/plot_classifier_comparison.html#sphx-glr-auto-examples-classification-plot-classifier-comparison-py)
