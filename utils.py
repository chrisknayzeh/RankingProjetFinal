import random
import numpy as np

#Function that reads a text file and returns the lines in a list, the number of rows and columns (in this case, row = col)
def readText(file):
  text = open(file)
  lines = text.readlines()
  row = int(lines[0])

  return lines, row

# Function to Print data in matrix form
def printMat(matrix):
  rows = []
  for i in range(len(matrix)):
    rows.append(matrix[i])
  
  for i in range(len(matrix)):
    print(rows[i] , "\n")

#Function to Remove spaces and new lines from linesz

def rmRed(lines):
  nodes = lines[0]
  total_edges= lines[1]
  newlines = list(lines[i] for i in range(2,len(lines)))
  
  #Using the " " as a delimiter for new elements. Each number will become an element on its own, and newlines will become a list of lists
  for i in range(len(newlines)):
    newlines[i] = newlines[i].split(" ")

  for line in newlines:
     #print(type(line))
     line.remove('\n')
     while ('' in line):
        line.remove('')
  return list(newlines), int(nodes), int(total_edges)

def convertStrNum(newlines):
  for i in range(len(newlines)):
    for j in range(len(newlines[i])):
      if(j<3 or j%2==0): #since we start indexing at 0, and we are interested in the values starting the third element, any values before the third element will become int.
                       #Also if the value is on an even index (0, 2, 4, 8 etc.) it will also be an int since it's either the row number, number of edges or a vertex number.
                       newlines[i][j] = int(newlines[i][j])
      else:
        newlines[i][j] = float(newlines[i][j]) #Otherwise, the rest of the values are the probabilities (or weights)
  return newlines

#Creating a random selector

def randSelect(N):
  return random.randint(0,N-1)

def randEdge(threshold): #returns true if edge is removed, false if not
  x = random.uniform(0,1)
  if x < threshold:
    return True
  else:
    return False