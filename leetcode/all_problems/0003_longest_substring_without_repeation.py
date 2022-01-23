from curses import window


class Solution:
    def longest_substring_without_repeation(self, s: str = "") -> int:

        l = 0
        res = 0
        char_set = set()

        for r in range(len(s)):
            while s[r] in char_set:
                char_set.remove(s[l])
                l += 1
            char_set.add(s[r])
            window_size = r - l + 1
            res = max(res, window_size)
        return res


def main():
    sl = Solution()
    s = "pwwkew"
    s = "abcabcbb"
    print(sl.longest_substring_without_repeation(s))


if __name__ == "__main__":
    main()
