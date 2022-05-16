class Solution:
        def lengthOfLongestSubstring(self, s:str) -> int:    
        window = set()
        lft_i = 0
        res = 0
        for rgt_i in range(len(s)):               
            while s[rgt_i] in  window:
                window.remove(s[lft_i])
                lft_i += 1
            window.add s[rgt_i]
            res = max( res, rgt_i - lft_i + 1)
        return res