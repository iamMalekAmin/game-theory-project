""" numOfUser , numOfActionForAllUser , values """
from matplotlib.pyplot import step
import numpy as np

numOfUser = int(input("Enter the number of user: "))

numOfAction = []

for i in range(numOfUser):
    action = int(input("Enter the number of action: "))
    numOfAction.append(action)

values = np.zeros((numOfAction[-1] , numOfUser))

for i in range(numOfAction[-1]):
    for j in range(numOfUser):
        num = int(input("Enter value : "))
        values[i][j] = num



temp = values

counter = 1
counterForPlayer = numOfAction[-1]
counter2 = numOfUser-1
maximumRoot = []

numberOfSteps = counterForPlayer
tempArr = []

for k in range(numOfUser):
    for i in range(counterForPlayer):
        for j in range(numOfUser):
            """ Take two lists """
            maximum = []
            if values[i][counter2] > values[i+1][counter2]:
                maximum = values[i]
            else:
                maximum = values[i+1]
        values[i] = maximum
        values = np.delete(values , i+1 , 0)
    counter2 = counter2 - 1
    counterForPlayer = counterForPlayer[-1] - 1 

    

print(values)    