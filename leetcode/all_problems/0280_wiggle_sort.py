from typing import List


class Solution:
    def wiggle_sort(self, nums: List[int]) -> List[int]:

        for i in range(1, len(nums)):
            if (i % 2 == 1 and nums[i] < nums[i - 1]) or (
                i % 2 == 0 and nums[i] > nums[i - 1]
            ):
                nums[i], nums[i - 1] = nums[i - 1], nums[i]
        return nums


def main():
    sl = Solution()
    nums = [3, 5, 2, 1, 6, 4]
    print(sl.wiggle_sort(nums=nums))


main()
