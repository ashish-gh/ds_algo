# Time complexity: O(v+e)


class Solution:
    def valid_tree(self, n, edges):
        if not n:
            return False
        
        adj = {i:[] for i in range(n)}
        for n1, n2 in edges:
            # each edge is connected to every node
            adj[n1].append(n2)
            adj[n2].append(n1)

        visits = set()
        def dfs(i, prev):
            if i in visits:
                # this is because we have already visited the node and 
                # don't want to loop over it agian and again
                return False
            visits.add(i)
            for j in adj[i]:
                # get the values of the neightbor
                if j == prev:
                    # checking if the previous node and the current node are the same
                    continue
                if not dfs(i, j):
                    # the neighbour we currently are in the loop and want to end the loop
                    return False
            return True
        return dfs(0, -1) and len(visits) == n                


