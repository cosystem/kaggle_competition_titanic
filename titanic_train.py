import os
import pandas

# read data file
__dir__ = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(__dir__, "train.csv")
titanic = pandas.read_csv(filepath)
# Print the first 5 rows of the dataframe.
print(titanic.head(10))

# Replace missing value in "Age" with the median value
titanic["Age"] = titanic["Age"].fillna(titanic["Age"].median())
print(titanic.describe())

# class to assign labels
class labelassign():
    # initialized varialbes
    def __init__(self, inString):
        self.assignlabel = inString
        self.uniquelist = list(titanic["Sex"].unique())
        self.numberlist = list(range(len(self.uniquelist)))
        self.package = (self.uniquelist, self.numberlist)

    # function to assign labels
    def assign(self, inTuple, remainnumber):
        if len(inTuple[0]) > remainnumber:
            label = inTuple[0].pop(0)
            number = inTuple[1].pop(0)
            titanic.loc[titanic[self.assignlabel] == self.assignlabel, self.assignlabel] = number
            self.assign(inTuple, remainnumber)


# Find all the unique genders, and assign label
print(titanic["Sex"].unique())
ToAssign = labelassign("Sex")
ToAssign.assign(ToAssign.package, 0)
print(titanic["Sex"].unique())
print(ToAssign.package)
print(type(ToAssign.assignlabel))
print(ToAssign.uniquelist)
print(ToAssign.numberlist)
print(list(titanic["Sex"].unique()))
print(type(titanic))
# Find all the unique Embark, and assign label
# print(titanic["Embarked"].unique())
# tupleEmbar=packgen("Embarked")
# assign(tupleEmbar, 1, "Embarked")
# print(titanic["Embarked"].unique())
