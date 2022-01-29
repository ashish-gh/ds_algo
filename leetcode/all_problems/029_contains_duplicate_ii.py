from typing import List


class Solution:
    def contains_duplicate(self, nums: List[int], k: int) -> bool:
        hash_map = {}
        for i, num in enumerate(nums):
            if (num in hash_map) and (i - hash_map[num]) <= k:
                return True
            hash_map[num] = i
        return False


def main():
    sl = Solution()
    nums = [1, 2, 3, 1]
    print(sl.contains_duplicate(nums, 3))


main()
