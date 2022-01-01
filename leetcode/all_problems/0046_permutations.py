# Given an array return the permutations of the numbers, this can be in any order



from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        if len(nums) == 1:
            return [nums[:]]
        
        for i in range(len(nums)):
            n = nums.pop(0)
            perms = self.permute(nums)

            for perm in perms:
                perm.append(n)
            result.extend(perms)
            nums.append(n)
        return result


class Solution1:
    def __init__(self) -> None:
        self.res = []

    def permute(self, nums, path):
        self.backtrack(nums, path)
        return self.res
    
    def backtrack(self, nums, path):
        if not nums:
            self.res.append(path)
        print(f"Nums <<<<<<<<<<< {nums}")
        for i in range(len(nums)):
            new_path= path + [nums[i]]
            print(f"New path : {new_path}")
            nums_ = nums[:i] + nums[i+1:]
            print(f"{nums[:i] }  | {nums[i+1:]} | Nums : {nums_}")
            self.backtrack(nums_, new_path)


def main():
    sl = Solution1()
    nums = [1,2,3]
    print(sl.permute(nums, []))


if __name__ =="__main__":
    main()
    