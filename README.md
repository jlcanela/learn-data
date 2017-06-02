# Learn data science and machine learning

## Learn Python for Data science #2

[Learn Python for Data science #2](https://www.youtube.com/watch?v=o_OZdbCzHUA&index=2&list=PL2-dafEMk2A6QKz1mrk1uIGfHkC1zZ6UU)

Registered my twitter app and used environment to setup config and avoid storing credentials in public github.

### Playing with the provided code 

What did I learn ?

* Textblob very easy to use, based on nltk, need to download data before using it with
* but not convinced by sentiment analysis with bag of words ([see counter example](http://blog.leenhardt.name/post/2008/10/21/Twittratr-%3A-how-to-make-a-fuzz-over-nothing))

To download nltk data:
```
import nltk
nltk.download()
```

### The challenge

1. Copy paste the demo.py file
1. Register twitter app
1. Configure credentials with environment variables
1. Use csv library, caution, need to use 'w' and not 'wb' for file modifier with python3

Siraj provide some documentation:
* Some details about Sentiment Analysis: https://www.quora.com/How-does-sentiment-analysis-work
* alchemylanguage which have been superseded by [watson](https://www.ibm.com/watson/developercloud/alchemy-language.html)


Code:

* [Github source code](https://github.com/jlcanela/learn-data/tree/master/learn-python-for-data-science-2)


Documentation:

* About TextBlob: https://textblob.readthedocs.io/en/dev/
* Awesome standford course: http://cs224d.stanford.edu/syllabus.html

## Learn Python for Data science #1

[Learn Python for Data science #1](https://www.youtube.com/watch?v=T5pRlIbr6gg)

Siraj's videos are awesome :)))), @Siraj, when you come to Paris ping me and let's have a drink, you rock !

### Playing with the provided code 

What did I learn ?

* Thanks to some tipos in buggy.py, I discovered that when data are incoherent, DecisionTreeClassifier.predict is returning sometimes 'male', sometimes 'female'
  * caused by mismatch in both X and Y values
  * DecisionTreeClassifier is using [numpy.random.RandomState](https://docs.scipy.org/doc/numpy/reference/generated/numpy.random.RandomState.html) according to [doc](http://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html) 
  * It's *really* *important* to **always** test the model and not starting to code without checking the data manually
* About testing
  * [unittest](https://docs.python.org/3/library/unittest.html) is fine to start with
  * Python ecosystem have [a lot](https://wiki.python.org/moin/PythonTestingToolsTaxonomy) of testing tools
  * I'll probably use [behave](https://pypi.python.org/pypi/behave), a BDD style library, later
* About Visual Studio Code
  * I used it for nodeJS development, but look good for python too
  * pylint enabled by default

### The challenge

1. Use any 3 SciKit-Learn models on this dataset
1. Compare results
1. Print the best one

First I dig through the scikit [doc](http://scikit-learn.org/stable/documentation.html) which looks very good.
I find a [classifier.py](learn-python-for-data-science-1/classifiers.py) code from [classifier comparison page](http://scikit-learn.org/stable/auto_examples/classification/plot_classifier_comparison.html#sphx-glr-auto-examples-classification-plot-classifier-comparison-py).

Siraj provided a link to [choose the right estimator](http://scikit-learn.org/stable/tutorial/machine_learning_map/). According to the link for classification with low number of sample: 
* try with [Linear SVC](http://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVC.html#sklearn.svm.LinearSVC)
* if not ok as not text data, try with [KNeighbors](http://scikit-learn.org/stable/modules/neighbors.html)
* if still not ok last chance are [SVC](http://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn.svm.SVC) or [ensemble](http://scikit-learn.org/stable/modules/ensemble.html) classifiers

Data set is very small, it seems that decision tree, KNeighbors or SVC are OK. Unfortunately LinearSVC is not OK. 

Code:

* [Github source code](https://github.com/jlcanela/learn-data/tree/master/learn-python-for-data-science-1)


Documentation:

* [Scikit documentation](http://scikit-learn.org/stable/user_guide.html) to find alternate models
* [Docstring conventions](https://www.python.org/dev/peps/pep-0257/) helpfull to fix pylint errors

# Tips

## Visual Studio Code - [pylint] C0103:Invalid constant name "clf"

According to [stack overflow](https://stackoverflow.com/questions/25184097/pylint-invalid-constant-name) when a name is not inside a function/class it is considered as a constant. 

Regex to check constant name is ```(([A-Z_][A-Z0-9_]*)|(__.*__))$```. I found it in [pylint documentation](http://pylint-messages.wikidot.com/messages:c0103).

Assuming we cannot change the code, what is the alternate option ? 

First generate a .pylintrc file:
```
pylint --generate-rcfile > .pylintrc
```

and then add C0103 to disable:
```
disable=C0103,print-statement,parameter-unpacking,unpacking-in-except,old-raise-syntax,backtick,import-star-module-level,apply-builtin,basestring-builtin,buffer-builtin,cmp-builtin,coerce-builtin,execfile-builtin,file-builtin,long-builtin,raw_input-builtin,reduce-builtin,standarderror-builtin,unicode-builtin,xrange-builtin,coerce-method,delslice-method,getslice-method,setslice-method,no-absolute-import,old-division,dict-iter-method,dict-view-method,next-method-called,metaclass-assignment,indexing-exception,raising-string,reload-builtin,oct-method,hex-method,nonzero-method,cmp-method,input-builtin,round-builtin,intern-builtin,unichr-builtin,map-builtin-not-iterating,zip-builtin-not-iterating,range-builtin-not-iterating,filter-builtin-not-iterating,using-cmp-argument,long-suffix,old-ne-operator,old-octal-literal,suppressed-message,useless-suppression
```

*et voila* !