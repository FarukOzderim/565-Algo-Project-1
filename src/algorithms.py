"""
Contains multiple algorithms for Max Leaf Spanning Tree problem. Each problem takes adjacency matrix as the input
and returns
1. tree(adjacency list)
2. number of leaves and vertices
"""

from typing import List


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
