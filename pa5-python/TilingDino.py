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


def create_graph(a):

    g = nx.DiGraph()
    w = len(a[0]) + 1
    h = len(a) + 1
    for y in range(h):
        for x in range(w):
            z = w * y + w

            if (x == 0 and y == h - 1) or (x == 0 and y == 0) or (x == w - 1 and y == 0) or (
                    x == w - 1 and y == h - 1):
                nx = 1
                ny = 1

                if x == w - 1:
                    nx = -1
                if y == h - 1:
                    ny = -1
                g.add_edge(z, z + nx, capacity=(a[y][x] == a[y][x + nx]))
                g.add_edge(z, z + (ny * w), capacity=(a[y][x] == a[x + ny][x]))
                g.add_edge(z, z + (ny * w) + nx, capacity=(a[y][x] == a[y + ny][x + nx]))

    return g


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
