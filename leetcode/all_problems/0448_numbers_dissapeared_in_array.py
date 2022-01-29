from typing import List


class Solution:
    def missing_array(self, nums: List[int]) -> List[int]:

        res = []
        for i in range(1, len(nums) + 1):
            if i not in nums:
                res.append(i)
        return res


def main():
    sl = Solution()
    nums = [4, 3, 2, 7, 8, 2, 3, 1]
    print(sl.missing_array(nums))


main()
