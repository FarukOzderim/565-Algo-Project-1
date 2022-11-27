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

    parent = list(
        np.zeros(
            100,
        )
    )
    d = list(
        np.zeros(
            100,
        )
    )
    size = list(
        np.zeros(
            100,
        )
    )
    find_parent_special = list(
        np.zeros(
            100,
        )
    )
    size1 = list(
        np.zeros(
            100,
        )
    )

    @staticmethod
    def reset():
        Approximationalgo.parent = list(
            np.zeros(
                100,
            )
        )
        Approximationalgo.d = list(
            np.zeros(
                100,
            )
        )
        Approximationalgo.size = list(
            np.zeros(
                100,
            )
        )
        Approximationalgo.find_parent_special = list(
            np.zeros(
                100,
            )
        )
        Approximationalgo.size1 = list(
            np.zeros(
                100,
            )
        )

    @staticmethod
    def findparent(v):

        v = int(v)

        if v == Approximationalgo.parent[v]:
            return v
        Approximationalgo.parent[v] = Approximationalgo.findparent(
            Approximationalgo.parent[v]
        )
        return Approximationalgo.parent[v]

    @staticmethod
    def unionbyrank(u, v):
        a = Approximationalgo.findparent(u)
        b = Approximationalgo.findparent(v)
        if a != b:
            if Approximationalgo.size[a] > Approximationalgo.size[b]:
                Approximationalgo.parent[b] = a
                Approximationalgo.size[a] = (
                    Approximationalgo.size[a] + Approximationalgo.size[b]
                )
            else:
                Approximationalgo.parent[a] = b
                Approximationalgo.size[b] = (
                    Approximationalgo.size[a] + Approximationalgo.size[b]
                )

    @staticmethod
    def buildMaximallyLeafyForest(vertex_count, G):
        F = []
        for i in range(vertex_count):
            Approximationalgo.d[i] = 0
            Approximationalgo.parent[i] = i
            Approximationalgo.size[i] = 1

        for i in range(vertex_count):
            s1 = []
            d1 = 0

            v = i
            for j in range(len(G[i])):
                u = G[i][j]
                if (
                    Approximationalgo.findparent(u) != Approximationalgo.findparent(v)
                    and [u, Approximationalgo.findparent(u)] not in s1
                ):
                    d1 = d1 + 1
                    s1.append([u, Approximationalgo.findparent(u)])

            if Approximationalgo.d[v] + d1 >= 3:
                for edge_pair in s1:

                    F.append([v, edge_pair[0]])
                    F.append([edge_pair[0], v])
                    Approximationalgo.unionbyrank(v, edge_pair[1])
                    Approximationalgo.d[edge_pair[0]] = (
                        Approximationalgo.d[edge_pair[0]] + 1
                    )
                    Approximationalgo.d[v] = Approximationalgo.d[v] + 1
        return F

    @staticmethod
    def findfind_parent_special(x):
        if Approximationalgo.find_parent_special[x] == x:
            return x
        Approximationalgo.find_parent_special[
            x
        ] = Approximationalgo.findfind_parent_special(
            Approximationalgo.find_parent_special[x]
        )
        return Approximationalgo.find_parent_special[x]

    @staticmethod
    def unionbyrank1(u, v):
        a = Approximationalgo.findfind_parent_special(u)
        b = Approximationalgo.findfind_parent_special(v)
        if a != b:
            if Approximationalgo.size1[a] > Approximationalgo.size1[b]:
                Approximationalgo.find_parent_special[b] = a
                Approximationalgo.size1[a] = (
                    Approximationalgo.size1[a] + Approximationalgo.size1[b]
                )
            else:
                Approximationalgo.find_parent_special[a] = b
                Approximationalgo.size1[b] = (
                    Approximationalgo.size1[a] + Approximationalgo.size1[b]
                )

    @staticmethod
    def kruskal(vertex_count, F):
        spanning_tree = []
        for i in range(vertex_count):
            Approximationalgo.find_parent_special[i] = i
        for edge in F:
            x = edge[0]
            y = edge[1]
            if Approximationalgo.findfind_parent_special(
                x
            ) != Approximationalgo.findfind_parent_special(y):
                spanning_tree.append([x, y])
                Approximationalgo.unionbyrank1(x, y)
        return spanning_tree

    @staticmethod
    def solve(prob_in):
        Approximationalgo.reset()
        G = []
        edge_list = []
        prob_copy = prob_in.copy()
        vertex_count = len(prob_copy)
        vertex_count += 1
        for vertex, connecting_vertex in prob_copy.items():
            for vertex_ in connecting_vertex:
                if vertex_ > vertex:
                    edge_list.append([vertex, vertex_])

        edge_count = len(edge_list)

        j = 0
        for i in range(100005):
            G.append([])
        for i in range(edge_count):
            x = edge_list[i]
            G[x[0]].append(x[1])
            G[x[1]].append(x[0])

        F = Approximationalgo.buildMaximallyLeafyForest(vertex_count, G)

        verticesinF = []

        for edge in F:
            verticesinF.append(edge[0])
            verticesinF.append(edge[1])

        for i in range(vertex_count):
            for j in range(len(G[i])):
                u = i
                v = G[i][j]

                if (u not in verticesinF) and (v not in verticesinF):
                    F.append([u, v])
                    F.append([v, u])

                elif Approximationalgo.findparent(u) != Approximationalgo.findparent(v):
                    F.append([u, v])
                    F.append([v, u])

        result = Approximationalgo.kruskal(vertex_count, F)

        dict = {}

        for edge in result:

            if dict.get(edge[0]) == None:
                dict.update({edge[0]: [edge[1]]})
            else:
                dict.get(edge[0]).append(edge[1])

            if dict.get(edge[1]) == None:
                dict.update({edge[1]: [edge[0]]})

            else:
                dict.get(edge[1]).append(edge[0])

        return dict
