# Hand-coding solutions for the Abstraction and Reasoning Corpus

This repository contains the solutions for some of the tasks created in the project **“Abstraction and Reasoning Corpus” (ARC)**. This project can be found and cloned from the following link  [https://github.com/jmmcd/ARC](https://github.com/jmmcd/ARC).

This set of task consist in a set of grids (2D arrays) where each  element is a number that represents the color of the cell.These grids contain patterns that can be transformed using a function *f(x)* that generates another grid. To find *f(x)* it is necessary to observe the given examples (at least 1 pair of input and output grids) and identify the pattern used to transform the grids.

![test space](https://bdtechtalks.com/wp-content/uploads/2019/12/ARC-example-1.png)

These tasks are designed to be solved by either by humans or computers (programs). Humans are able to solve them by intuition beased on the knwoledge adquired during their live to identify shapes, patterns,solving problem skills,etc. (without a formal definition of a function or and algorithm).

For this project the programmer(s) has to find the pattern for each task observing the different inputs and outputs to create a function that could transform the given training examples and other inputs with similar characteristics(can be transformed using the same function).

The file `src/manual solve.py` contains the functions that solves some of the tasks. There is a function `solve_<task-id>(x)` for each solved task. All the implemented functions contains:
- Description of the algorithm implemented to solve the task
- Relevant comments taht describe the steps followed
- Asserts statements to test the function and verify that solves the training grids
- Statement that returns the generated grid (transformed)

The project contains a wide variety of tasks based than could be classified based on the complexity:
- Easy
- Medium
- Medium-to-difficult
- Difficult

The tasks are stored in JSON format. Each task JSON file contains a dictionary with two fields:

- `"train"`: demonstration input/output pairs. It is a list of "pairs" (typically 3 pairs).
- `"test"`: test input/output pairs. It is a list of "pairs" (typically 1 pair).

The original project also contians a web page that runs locally (no server application is needed) to visualize and solves the tasks manually located at `apps/testing_interface.html`
