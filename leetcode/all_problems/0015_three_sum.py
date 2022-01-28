from typing import List


class Solution:
    def three_sum(self, nums: List[int]) -> List[List[int]]:
        """
        """
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if i > 0 and nums[i - 1] == a:
                # if the previous and current element is same we just want to shift the pointer
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                three_sum = nums[l] + nums[r] + a
                if three_sum > 0:
                    r -= 1
                elif three_sum < 0:
                    l += 1
                else:
                    res.append([nums[l], nums[r], a])
                    l += 1
                    while nums[i] == nums[i - 1] and l < r:
                        l += 1
        return res
