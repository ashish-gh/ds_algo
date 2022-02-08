from typing import List


class Solution:
    def find_duplicates(self, nums: List[int]):
        res = []

        for num in nums:
            index = abs(num) - 1
            if nums[index] < 0:
                res.append(index + 1)
            else:
                nums[index] = num * -1
        return res


def main():
    sl = Solution()
    nums = [1, 2, 3, 4, 1, 2]
    res = sl.find_duplicates(nums=nums)
    print(res)


if __name__ == "__main__":
    main()
