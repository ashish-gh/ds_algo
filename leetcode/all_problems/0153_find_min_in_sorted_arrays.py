from typing import List


class Solution:
    def findmin(self, nums: List[int]) -> int:
        res = nums[0]
        l, r = 0, len(nums) - 1
        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            
            mid = (l + r) // 2
            res = min(res, nums[mid])

            if nums[mid] > nums[l]:
                l = mid + 1
            else:
                r = mid - 1
        return res



def main():
    nums = [3,4,5,1,2]
    sl = Solution()
    print(sl.findmin(nums=nums))

if __name__ == "__main__":
    main()
