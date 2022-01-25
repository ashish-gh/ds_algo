import re


class Solution:
    def num_encodin(self, s: str) -> int:
        dp = {len(s): 1}
        print(f"0 Initial : {dp}............")

        def dfs(i):
            if i in dp:
                print(f" 1. { dp[i]}  | {i} | {dp}")
                return dp[i]
            if s[i] == "0":
                return 0

            res = dfs(i + 1)
            if i + 1 < len(s) and (
                s[i] == "1" or s[i] == "2" and s[i + 1] in "0123456"
            ):
                print(f" 2.  | {i} | {dp}")
                res += dfs(i + 2)
            dp[i] = res
            print("3")
            return res

        return dfs(0)


def main():
    test = "1241"
    sl = Solution()
    print(sl.num_encodin(test))
    ...


if __name__ == "__main__":
    main()
