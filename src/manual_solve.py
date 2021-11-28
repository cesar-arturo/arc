#!/usr/bin/python

import os, sys
import json
import numpy as np
import re

"""
Student name(s): Cesar Arturo Alba Moreno
Student ID(s): 21251994
Git repository: https://github.com/cesar-arturo/arc

"""

### YOUR CODE HERE: write at least three functions which solve
### specific tasks by transforming the input x and returning the
### result. Name them according to the task ID as in the three
### examples below. Delete the three examples. The tasks you choose
### must be in the data/training directory, not data/evaluation.


def solve_b94a9452(x):
    """
    Description:
        The expected input for this task is a grid with squares of different color.There is an inner and outer square
        (one inside the other) and the orign is the same for both.
        The transformation removes the empty cells and keeps only the part of the grid that contains the squares. 
        Once the grid is "trimmed" the color of the squares is switched. 
    
    """
    # Trim the grid horizontally.Remove all rows that contains only 0.
    # np.all function will find what columns(depending on the given axis) contains only 0(given condition) and will
    # exclude them from the new grid
    x = x[~np.all(x == 0, axis=1)]
    #Trim the grid vertically.Remove all columns that contains only 0
    x = x[:,~np.all(x == 0, axis=0)]
    
    # Get the different colors of the grid
    colors= np.unique(x)
    # Switch colors using the np.where functions to do a simple replacement.
    # In this case the np.where works as a ternary operator switching the current value during the iteration
    x=np.where(x == colors[0], colors[1], colors[0])
    return x

def solve_6e19193c(x):
    """
    Description:
        The expected input for this task is a grid with at least 1 sequence of cells that generates a L shape(3 cells), 
        all of them have the same color.
        This shape could come in four rotations: 0,90,180,270 degrees.
        
        The transformation is a copy of the original grid(same size and the L's i the same position) but adding a diagonal line
        line for each L shape. The diagonals will be projected until the limit of the grid depending on the rotation in the following directions:
            0 degrees: Diagonal projected to the right top 
            90 degrees: Diagonal projected to the left top 
            180 degrees: Diagonal projected to the left bottom 
            270 degrees: Diagonal projected to the right bottom 
        The origin of the digonal line is the outer cell of the L shape realtive to the intersection.
    
    """
    # Get the general information of the grid : size and color of the L shapes
    # Store the size of the grid in two variables w(width) and h(height)
    w, h = x.shape
    # Get the different colors of the grid removing the blank color(0) to get the color of the shapes
    color= np.delete(np.unique(x), 0)[0]
    
    #Array to store all the x,y pairs that represents the origin of the diagonal lines
    origins=[]
    
    for j in range(w):
        for i in range(h):
            #Finds 2 consecutive filled cell in the x axis.There is an L shape
            if x[i][j]== color and j+1 <= w and x[i][j+1]== color:
                #Find the degrees of the shape
                #validate if it's an L 0 degrees
                if i - 1 >= 0 and  x[i-1][j]== color:
                    origins.append((0, i-1, j+1))
                #Validate if it's an L 90 degrees
                if i - 1 >= 0 and  x[i-1][j+1]== color:
                    origins.append((90, i-1, j))
                #Validate if it's an L 180 degrees
                if i + 1 <= h and  x[i+1][j+1]== color:
                    origins.append((180, i+1, j))
                #Validate if it's an L 270 degrees
                if i + 1 <= h and  x[i+1][j]== color:
                    origins.append((270, i+1, j+1))
                
    #For each origin draw a line
    # Depending on the direction of the line the limits must be checked to avoid out of bund errors
    for origin in origins:
        #0 degrees
        if origin[0]==0 and origin[1] - 1 >=0 and origin[2]+1 <= w :
            col_index=origin[2]+1;
            for i in range(origin[1] - 1, -1, -1):
                if(col_index <= w-1):
                    x[i][col_index]=color
                    col_index+=1
        #90 degrees
        if origin[0]==90 and origin[1] - 1 >=0 and origin[2]-1 >= 0 :
            col_index=origin[2]-1
            for i in range(origin[1] - 1, -1, -1):
                if(col_index >= 0):
                    x[i][col_index]=color
                    col_index-=1
        #180 degrees
        if origin[0]==180 and origin[1] + 1 <=h and origin[2]-1 >= 0 :
            col_index=origin[2]-1
            for i in range(origin[1] + 1, h, 1):
                if(col_index >= 0):
                    x[i][col_index]=color
                    col_index-=1
        #270 degrees
        if origin[0]==270 and origin[1] + 1 <=h and origin[2]+1 <= w :
            col_index=origin[2]+1
            for i in range(origin[1] + 1, h, 1):
                if(col_index <= w-1):
                    x[i][col_index]=color
                    col_index+=1
    return x

def main():
    # Find all the functions defined in this file whose names are
    # like solve_abcd1234(), and run them.

    # regex to match solve_* functions and extract task IDs
    p = r"solve_([a-f0-9]{8})" 
    tasks_solvers = []
    # globals() gives a dict containing all global names (variables
    # and functions), as name: value pairs.
    for name in globals(): 
        m = re.match(p, name)
        if m:
            # if the name fits the pattern eg solve_abcd1234
            ID = m.group(1) # just the task ID
            solve_fn = globals()[name] # the fn itself
            tasks_solvers.append((ID, solve_fn))

    for ID, solve_fn in tasks_solvers:
        # for each task, read the data and call test()
        directory = os.path.join("..", "data", "training")
        json_filename = os.path.join(directory, ID + ".json")
        data = read_ARC_JSON(json_filename)
        test(ID, solve_fn, data)
    
def read_ARC_JSON(filepath):
    """Given a filepath, read in the ARC task data which is in JSON
    format. Extract the train/test input/output pairs of
    grids. Convert each grid to np.array and return train_input,
    train_output, test_input, test_output."""
    
    # Open the JSON file and load it 
    data = json.load(open(filepath))

    # Extract the train/test input/output grids. Each grid will be a
    # list of lists of ints. We convert to Numpy.
    train_input = [np.array(data['train'][i]['input']) for i in range(len(data['train']))]
    train_output = [np.array(data['train'][i]['output']) for i in range(len(data['train']))]
    test_input = [np.array(data['test'][i]['input']) for i in range(len(data['test']))]
    test_output = [np.array(data['test'][i]['output']) for i in range(len(data['test']))]

    return (train_input, train_output, test_input, test_output)


def test(taskID, solve, data):
    """Given a task ID, call the given solve() function on every
    example in the task data."""
    print(taskID)
    train_input, train_output, test_input, test_output = data
    print("Training grids")
    for x, y in zip(train_input, train_output):
        yhat = solve(x)
        show_result(x, y, yhat)
    print("Test grids")
    for x, y in zip(test_input, test_output):
        yhat = solve(x)
        show_result(x, y, yhat)

        
def show_result(x, y, yhat):
    print("Input")
    print(x)
    print("Correct output")
    print(y)
    print("Our output")
    print(yhat)
    print("Correct?")
    if y.shape != yhat.shape:
        print(f"False. Incorrect shape: {y.shape} v {yhat.shape}")
    else:
        print(np.all(y == yhat))


if __name__ == "__main__": main()

