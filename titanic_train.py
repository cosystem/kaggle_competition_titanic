import os
import pandas
from collections import deque

# read data file
__dir__ = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(__dir__, "train.csv")
titanic = pandas.read_csv(filepath)
# Print the first 5 rows of the dataframe.
# print(titanic.head(10))

# Replace missing value in "Age" with the median value
titanic["Age"] = titanic["Age"].fillna(titanic["Age"].median())
# print(titanic.describe())

# function to generate tutple used in label assignment
def packgen(inString):
    uniquelist = deque(titanic[inString].unique())
    numberlist = deque(range(len(uniquelist)))
    package = (uniquelist, numberlist)
    return package

# function to assign labels
def assign(inTuple, remainnumber, assignlabel):
    if len(inTuple[0]) > remainnumber:
        label = inTuple[0].popleft()
        number = inTuple[1].popleft()
        titanic.loc[titanic[assignlabel] == label, assignlabel] = number
        assign(inTuple, remainnumber, assignlabel)

# Find all the unique genders, and assign label
print(titanic["Sex"].unique())
tupleSex=packgen("Sex")
assign(tupleSex, 0, "Sex")
print(titanic["Sex"].unique())

# Find all the unique Embark, and assign label
print(titanic["Embarked"].unique())
tupleEmbar=packgen("Embarked")
assign(tupleEmbar, 1, "Embarked")
print(titanic["Embarked"].unique())
