# Time Complexity: O(n)
class Solution:
    def longest_palindrome(self, s: str) -> str:

        if not s:
            return ""
        res = ""
        res_length = 0

        for i in range(len(s)):
            # check for odd case
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > res_length:
                    res = s[l : r + 1]
                    res_length = r - l + 1
                l -= 1
                r += 1

            # check for even case
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > res_length:
                    res = s[l : r + 1]
                    res_length = r - l + 1

                l -= 1
                r += 1
        return res


def main():
    res = "abacs"
    sl = Solution()
    print(sl.longest_palindrome(res))


if __name__ == "__main__":
    main()
