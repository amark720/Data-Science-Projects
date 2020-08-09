# Machine learning from disaster - Titanic predictions
This notebook uses the dataset from kaggle and tries to predict the survivals of the titanic incident. The survival are based on many features such as age, sex, fare, embarked etc.
Kaggle Competetion Link-> https://www.kaggle.com/c/titanic
My Solution Link -> https://www.kaggle.com/datawarriors/easy-beginner-titanic-solution

## Preprocessing and Feature Engineering
* Dropped 'Ticket' and 'Cabin' features
* Made a new feature 'Title' by using the 'Name' feature.
* Made a new ordinal feature 'Family_size' using 'Parch' and 'SibSp'.

Of course, this project requires some data cleaning and feature engineering as not all of the given data are useful. I used the most common ML algorithms (linear regression, k-means, Logistic Regression etc.) and I observed that Logistic Regression classifier is simple to use and works better than any alternative algorithm for this problem.
However we get More Accurate Predection using Deep Learning models!
