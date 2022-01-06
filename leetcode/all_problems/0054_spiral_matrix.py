#


from typing import List


class Solution:
    def spiral_matrix(self, nums: List[int]) -> List[int]:

        res = []
        left, right = 0, len(nums[0])
        top, bottom = 0, len(nums)

        while left < right and top < bottom:
            # from left to right
            for i in range(left,right):
                res.append(nums[top][i])
            top += 1

            # from top to bottom 
            for i in range(top, bottom):
                res.append(nums[i][right - 1])
            right -= 1

            if not (left < right and top < bottom):
                break

            # from right to the left
            for i in range(right - 1, left - 1, -1):
                res.append(nums[bottom - 1][i])
            bottom -= 1

            # from bottom to top
            for i in range(bottom -1, top -1, -1):
                res.append(nums[i][left])
            left += 1
        return res


def main():
    sl = Solution()
    nums =  [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    res = sl.spiral_matrix(nums)
    print(res)


if __name__ == "__main__":
    main()
            
            







