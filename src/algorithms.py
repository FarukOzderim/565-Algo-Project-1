"""
Contains multiple algorithms for Max Leaf Spanning Tree problem. Each problem takes adjacency matrix as the input
and returns
1. tree(adjacency list)
2. number of leaves and vertices
"""

from typing import List
import numpy as np


class SimpleGreedy:
    @staticmethod
    def solve(prob_in: dict) -> dict:
        """
        Simple greedy solution, similar to BFS.

        Args:
            prob_in: adjacency_list

        Returns:

        """
        # Create a copy of the problem and get some metadata
        prob_copy = prob_in.copy()
        vertex_count = len(prob_copy)
        # Create an empty tree to build
        tree = {}
        for i in range(vertex_count):
            tree[i] = []
        in_tree = [False for i in range(vertex_count)]
        # Need a list of candidates
        candidates = []

        # Find the root node
        root_vert = 0
        root_ecount = len(prob_copy[root_vert])
        for i in range(1, vertex_count):
            if len(prob_copy[i]) > root_ecount:
                root_vert = i
                root_ecount = len(prob_copy[i])
        candidates.append(root_vert)

        # Keep adding to tree until we run out
        while len(candidates) > 0:
            # Get ideal candidate and remove from list
            best = candidates[0]
            best_ecount = len(prob_copy[best])
            for i in candidates:
                if len(prob_copy[i]) > best_ecount:
                    best = i
                    best_ecount = len(prob_copy[i])
            candidates.remove(best)
            # print("Ideal candidate: {}".format(best))

            # Add ideal candidate's children to tree and list of candidates
            best_elist = prob_copy[best]
            in_tree[best] = True
            for item in best_elist:
                if not in_tree[item]:
                    in_tree[item] = True
                    tree[best].append(item)
                    tree[item].append(best)
                    candidates.append(item)
            # print("Candidate list 1: {}".format(candidates))

            # Prune candidates with no valid children
            c_copy = candidates.copy()
            for item in c_copy:
                adj_list = prob_copy[item]
                has_valid = False
                for child in adj_list:
                    if not in_tree[child]:
                        has_valid = True
                        continue
                if not has_valid:
                    candidates.remove(item)
            # print("Candidate list 2: {}".format(candidates))

        # Return the spanning tree

        return tree


class Approximationalgo:
    def __init__(self):
        self.parent = list(
            np.zeros(
                100,
            )
        )
        self.d = list(
            np.zeros(
                100,
            )
        )
        self.size = list(
            np.zeros(
                100,
            )
        )
        self.parent1 = list(
            np.zeros(
                100,
            )
        )
        self.size1 = list(
            np.zeros(
                100,
            )
        )

    def findparent(self, v):
        if v == self.parent[v]:
            return v
        self.parent[v] = self.findparent(self.parent[v])
        return self.parent[v]

    def unionbyrank(self, u, v):
        a = self.findparent(u)
        b = self.findparent(v)
        if a != b:
            if self.size[a] > self.size[b]:
                self.parent[b] = a
                self.size[a] = self.size[a] + self.size[b]
            else:
                self.parent[a] = b
                self.size[b] = self.size[a] + self.size[b]

    def buildMaximallyLeafyForest(self, noofvertices, G):
        F = []
        for i in range(noofvertices):
            self.d[i] = 0
            self.parent[i] = i
            self.size[i] = 1

        for i in range(noofvertices):
            s1 = []
            d1 = 0

            v = i
            for j in range(len(G[i])):
                u = G[i][j]
                if (
                    self.findparent(u) != self.findparent(v)
                    and [u, self.findparent(u)] not in s1
                ):
                    d1 = d1 + 1
                    s1.append([u, self.findparent(u)])
                    # s1 = s1.update({u : findparent(u)})

            if self.d[v] + d1 >= 3:
                for i in s1:
                    # F.update({v : i})
                    # F.update({i :  v})
                    # unionbyrank(v,s1.get(i))
                    # d[i] = d[i] + 1
                    # d[v] = d[v] + 1
                    F.append([v, i[0]])
                    F.append([i[0], v])
                    self.unionbyrank(v, i[1])
                    self.d[i[0]] = self.d[i[0]] + 1
                    self.d[v] = self.d[v] + 1
        return F

    def findparent1(self, x):
        if self.parent1[x] == x:
            return x
        self.parent1[x] = self.findparent1(self.parent1[x])
        return self.parent1[x]

    def unionbyrank1(self, u, v):
        a = self.findparent1(u)
        b = self.findparent1(v)
        if a != b:
            if self.size1[a] > self.size1[b]:
                self.parent1[b] = a
                self.size1[a] = self.size1[a] + self.size1[b]
            else:
                self.parent1[a] = b
                self.size1[b] = self.size1[a] + self.size1[b]

    def kruskal(self, noofvertices, F):
        spanningtree = []
        for i in range(noofvertices):
            self.parent1[i] = i
        for i in F:
            x = i[0]
            y = i[1]
            if self.findparent1(x) != self.findparent1(y):
                spanningtree.append([x, y])
                self.unionbyrank1(x, y)
        return spanningtree

    def solve(self, prob_in):

        G = []
        inputedges = []
        prob_copy = prob_in.copy()
        noofvertices = len(prob_copy)
        for i in prob_copy.keys():
            for j in prob_copy.get(i):
                if j > i:
                    inputedges.append([i, j])

        noofedges = len(inputedges)
        print(inputedges)
        j = 0
        for i in range(100005):
            G.append([])
        for i in range(noofedges):
            x = inputedges[i]
            G[x[0]].append(x[1])
            G[x[1]].append(x[0])

        F = self.buildMaximallyLeafyForest(noofvertices, G)

        verticesinF = []

        for i in F:
            verticesinF.append(i[0])
            verticesinF.append(i[1])

        for i in range(noofvertices):
            for j in range(len(G[i])):
                u = i
                v = G[i][j]

                if (u not in verticesinF) and (v not in verticesinF):
                    F.append([u, v])
                    F.append([v, u])

                elif self.findparent(u) != self.findparent(v):
                    F.append([u, v])
                    F.append([v, u])

        result = self.kruskal(noofvertices, F)

        dict = {}

        for i in result:
            if dict.get(i[0]) == None:
                dict.update({i[0]: [i[1]]})
            else:
                dict.get(i[0]).append(i[1])

            if dict.get(i[1]) == None:
                dict.update({i[1]: [i[0]]})
            else:
                dict.get(i[1]).append(i[0])
        return dict
