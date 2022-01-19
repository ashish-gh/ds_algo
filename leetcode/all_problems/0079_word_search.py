# Time Complexity:
# Space Complexity: 

# Stratgy: Recursive Backtracking | Depth First Search


from typing import List


class Solution:
    def exist(self, board: List[List[int]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        path = set()

        def dfs(r, c, i):
            if i == len(word): return True # visited every element of the word and found all the elements
            
            # check for the bound case
            if (
                r < 0 or c < 0 or # check for the bound 
                r >= rows or c >= cols or # check for the bound
                word[i] != board[r][c] or # make sure the letter we are searching is in the baord
                (r,c) in path # making sure the letter is not already visited
                ):
                return False
            
            path.add((r,c))

            res = (
                dfs(r + 1, c, i) or 
                dfs(r - 1, c, i) or 
                dfs(r, c + 1, i) or 
                dfs(r, c - 1, i) 
            )
            path.remove((r,c))
            return res
        
        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0): return True
        return False

        
