
import numpy as np
import pandas as pd

x = []

n = int(input("Enter number of player one: "))
m = int(input("Enter number of player two: "))

i = 0

while i < n:
  a = []
  j = 0
  while j < m:
    action1 = int(input ("Enter player 1 action: "))
    y = []
    y.append(action1)
    y.append(0)
    a.append(y)
    j = j + 1
  i = i + 1
  x.append(a)

i = 0


while i < n:
  j = 0
  while j < m:
    action2 = int(input ("Enter player 2 action"))
    x[i][j][1] = action2
    j = j + 1
  i = i + 1




drops = []

i = 0

while i < n:
  l1 = i
  k = i + 1
  while k < n:
    l2 = k
    j = 0
    while j < m:
      if x[i][j][0] <= x[k][j][0]:
        l2 = -1
      if x[k][j][0] <= x[i][j][0]:
        l1 = -1
      j = j +1
    if l1 != -1:
      drops.append(l1)
    if l2 != -1:
      drops.append(l2)
    k = k +1
  i = i +1
    
drops = list(set(drops))
matrix_data = np.delete(x , drops, axis=0)
n -= len(drops)
drops = []

i = 0

while i < m:
  l1 = i
  k = i+1
  while k < m:
    l2 = k
    j = 0
    while j < n:
      if x[j][i][1] <= x[j][k][1]:
        l2 = -1
      if x[j][k][1] <= x[j][i][1]:
        l1 = -1
      j = j +1
    if l1 != -1:
      drops.append(l1)
    if l2 != -1:
      drops.append(l2)
    k = k +1
  i = i +1
list_of_drops = list(set(drops))
matrix_data = np.delete(matrix_data, list_of_drops, axis=1)
m -= len(list_of_drops)


print(x)


drops = []
i = 0
while i < n:
  l1 = i
  k = i + 1
  while k < n:
    l2 = k
    b1 = 0
    b2 = 0
    j = 0 
    while j < m:
      if x[i][j][0] > x[k][j][0]:
        b2 = 1
      if x[i][j][0] < x[k][j][0]:
        l2 = -1
      if x[k][j][0] > x[i][j][0]:
        b1 = 1
      if x[k][j][0] < x[i][j][0]:
        l1 = -1
      j = j + 1
    if l1 != -1 and b1 == 1:
      drops.append(l1)
    if l2 != -1 and b2 == 1:
      drops.append(l2)
    k = k + 1
  i = i + 1
drops = list(set(drops))
x = np.delete(x, drops, axis=0)
n -= len(drops)
drops = []
i = 0
while i < m:
  l1 = i
  k = i + 1
  while k < m:
    l2 = k
    b1 = 0
    b2 = 0
    j = 0
    while j < n:
      if x[j][i][1] > x[j][k][1]:
        b2 = 1
      if x[j][i][1] < x[j][k][1]:
        l2 = -1
      if x[j][k][1] > x[j][i][1]:
        b1 = 1
      if x[j][k][1] < x[j][i][1]:
        l1 = -1
      j = j +1
    if l1 != -1 and b1 == 1:
      drops.append(l1)
    if l2 != -1 and b2 == 1:
      drops.append(l2)
    k = k + 1
  i = i + 1
drops = list(set(drops))
matrix_data = np.delete(matrix_data, drops, axis=1)
m -= len(drops)


print(x)
