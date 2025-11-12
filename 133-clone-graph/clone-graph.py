"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        oldToNew = {}

        def dfs(old):
            if old in oldToNew:
                return oldToNew[old]
            
            new = Node(old.val)
            oldToNew[old] = new

            for neighbor in old.neighbors:
                newNeighbor = dfs(neighbor)
                new.neighbors.append(newNeighbor)

            return new

        return dfs(node) if node else None