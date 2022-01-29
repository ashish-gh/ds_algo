from typing import List


class Solution:
    def contains_duplicate(self, nums: List[int]) -> bool:

        # Method 1 : Hash map or hash set
        # Time Complexity: O(n) | Space Complexity O(n)
        hash_map = {}
        for num in nums:
            if num in hash_map:
                return True
            hash_map[num] = True
        return False

        # Method 2
        # Sort and check first and second index
        # Time Complexity: O(n log n) * O(n)  | Space Complextiy : O(1)
        # nums.sort()
        # for i in range(len(nums) - 1):
        #     if nums[i] == nums[i + 1]:
        #         return True
        # return False


def main():
    sl = Solution()
    nums = [1, 2, 4, 1]
    print(sl.contains_duplicate(nums))


main()
