# Question:


from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[int]:
        # check base case
        if len(nums) == 1: return [nums[:]]
        
        result = []
        for _ in range(len(nums)):

            # pop the first elements of the list and 
            # for the remaining elements find the permutation by recursive methods
            n = nums.pop(0)
            perms = self.permute(nums=nums)
            # for every new permutatio, we append the popped previous element to the new permutation
            for perm in perms:
                perm.append(n)
            # now every permutation is extended to the final results
            result.extend(perms)
            # append the popped element back to the nums
            nums.append(n)
        return result
        

def main():
    sl = Solution()
    nums = [1,1,3]
    res  = sl.permute(nums=nums)
    print(f"List of perms : {res}")


if __name__ == "__main__":
    main()