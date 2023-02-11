#-------------------------------------------------------------------------
# AUTHOR: your name
# FILENAME: title of the source file
# SPECIFICATION: description of the program
# FOR: CS 4210- Assignment #1
# TIME SPENT: how long it took you to complete the assignment
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard
# dictionaries, lists, and arrays

#importing some Python libraries
from sklearn import tree
import matplotlib.pyplot as plt
import csv
db = []

#reading the data in a csv file
with open('contact_lens.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i > 0: #skipping the header
         db.append (row)
         #print(row)
X = [] #to store the training features
Y = [] #to store the training class labels
#transform the original categorical training features into numbers and add to the 4D array X. For instance Young = 1, Prepresbyopic = 2, Presbyopic = 3
# so X = [[1, 1, 1, 1], [2, 2, 2, 2], ...]]
for i, row in enumerate(db):
  X.append([])
  match row[0]:
    case 'Young':
      X[i].append(1)
    case 'Prepresbyopic':
      X[i].append(2)
    case 'Presbyopic':
      X[i].append(3)
    case _: # default
      X[i].append(0)

  #Spectacle
  match row[1]:
    case 'Myope':
      X[i].append(1)
    case 'Hypermetrope':
      X[i].append(2)
    case _: # default
      X[i].append(0)
  
  #Astigmatism
  match row[2]:
    case 'Yes':
      X[i].append(1)
    case 'No':
      X[i].append(2)
    case _: # default
      X[i].append(0)

  #Tear Production Rate
  match row[3]:
    case 'Reduced':
      X[i].append(1)
    case 'Normal':
      X[i].append(2)
    case _: # default
      X[i].append(0)

  #transform the original categorical training classes into numbers and add to the vector Y. For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
  #Recomendation
  match row[4]:
    case 'Yes':
      Y.append(1)
    case 'No':
      Y.append(2)
    case _: # default
      Y.append(0)


print(X)
print(Y)
#fitting the decision tree to the data
clf = tree.DecisionTreeClassifier(criterion = 'entropy')
clf = clf.fit(X, Y)

#plotting the decision tree
tree.plot_tree(clf, feature_names=['Age', 'Spectacle', 'Astigmatism', 'Tear'], class_names=['Yes','No'], filled=True, rounded=True)
plt.show()