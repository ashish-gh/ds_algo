class Solution:

    def is_palindrom(self, s: str) -> bool:

        l, r = 0, len(s) - 1
        
        while l < r:
            while l < r and not self.alpha_num(s[l]):
                l +=1
            
            while r > l and not self.alpha_num(s[r]):
                r -=1
            
            if self.alpha_num(s[l])  != self.alpha_num(s[r]):
                return False            
            l -= 1
            r += 1            
        return True
            
        

    def alpha_num(self, char: str):
        return (
            ord("A") <= ord(char) <= ord("Z") or
            ord("a") <= ord(char) <= ord("z") or
            ord("0") <= ord(char) <= ord("9") or
        )
