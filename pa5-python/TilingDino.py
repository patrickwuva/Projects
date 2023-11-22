# CS3100 - Fall 2023 - Programming Assignment 5
#################################
# Collaboration Policy: You may discuss the problem and the overall
# strategy with up to 4 other students, but you MUST list those people
# in your submission under collaborators.  You may NOT share code,
# look at others' code, or help others debug their code.  Please read
# the syllabus carefully around coding.  Do not seek published or online
# solutions for any assignments. If you use any published or online resources
# (which may not include solutions) when completing this assignment, be sure to
# cite them. Do not submit a solution that you are unable to explain orally to a
# member of the course staff.
#################################
# Your Computing ID: 
# Collaborators: 
# Sources: Introduction to Algorithms, Cormen
#################################
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import PIL
import math
from copy import deepcopy
from collections import deque
from networkx.algorithms.flow import dinitz


def create_array(lines):
    arr = []
    for _ in lines:
        arr.append([])

    for i in range(len(arr)):
        for s in lines[i]:
            if s == ".":
                arr[i].append(0)
            else:

                arr[i].append(1)
    return arr


def create_graph(a):
    g = nx.DiGraph()

    for i in range(len(a)):
        for j in range(len(a[i])):

            if i == 0:
                if j == 0:
                    g.add_edge(j, i, capacity=a[j][i] == a[i][j + 1])
                if j == len(a[i]) - 1:
                    g.add_edge(j, i, capacity=a[j][i] == a[i][j - 1])
            elif i == len(a) - 1:
                if j == 0:
                    g.add_edge(j, i, capacity=a[j][i] == a[i][j + 1])
                if j == len(a[i]) - 1:
                    g.add_edge(j, i, capacity=a[j][i] == a[i][j - 1])

            else:
                if j == 0:
                    g.add_edge(j, i, capacity=(a[j][i] == a[i][j + 1] and a[i][j] == a[i][j - 1] and a[i][j] == a[i-1][j - 1] and a[i][j] == a[i-1][j + 1] and a[i][j] == a[i-1][j]))
                if j == len(a[i]) - 1:
                    g.add_edge(j, i, capacity=a[i][j] == a[i][j - 1])
    return g


class TilingDino:
    def __init__(self):
        return

    # This is the method that should set off the computation
    # of tiling dino.  It takes as input a list lines of input
    # as strings.  You should parse that input, find a tiling,
    # and return a list of strings representing the tiling
    #
    # @return the list of strings representing the tiling
    def compute(self, lines):
        m = create_array(lines)
        g = create_graph(m)

        print(g.number_of_edges())
        for r in m:
            print(r)
        return ["impossible"]
