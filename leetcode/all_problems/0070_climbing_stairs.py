class Solution:
    def climb_stairs(self, num: int) -> int:
        one, two = 1, 1
        for i in range(num - 1):
            temp = one
            one = one + two
            two = temp
        return one


def main():
    sl = Solution()
    num = 5
    print(sl.climb_stairs(num))


main()
