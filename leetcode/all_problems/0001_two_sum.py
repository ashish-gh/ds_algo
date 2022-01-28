# Time Complexity: O(n)
# Space Complexity: O(n)


from typing import List


class Solution:
    def two_sum(self, nums: List[int], target: int) -> List[int]:

        hash_map = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in hash_map:
                return [hash_map[diff], i]
            hash_map[num] = i
        return None


def main():
    sl = Solution()
    nums = [2, 7, 11, 15]
    target = 9
    print(sl.two_sum(nums=nums, target=target))


main()
