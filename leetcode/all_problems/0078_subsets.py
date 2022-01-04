# Question 

# 


# Answers:


from typing import List


class Solutions:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subsets = []
        def dfs(i):
            # check for out of bounds
            if i >= len(nums):
                # we don't want to change the initial subset but want to append the copy of the current subset to the results.
                res.append(subsets.copy())
                return            
            # decision to include nums[i], to include the left most elements
            subsets.append(nums[i])
            dfs(i+1)
            # decision not to include nums[i]
            subsets.pop()
            # this recursive call will have empty subset given to it
            dfs(i + 1)
        # call with initals values and return the result
        dfs(0)
        return res

            
def main():
    
    pass

if __name__ == "__main__":
    main()