class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        longest = 0
        mp = {}

        checking = True
        while checking:
            try:
                if s[r] not in mp:
                    mp[s[r]] = r
                    r += 1
                else:
                    longest = max(len(s[l:r]), longest)
                    l = mp[s[r]] + 1
                    r = l
                    mp = {}
            except:
                longest = max(len(s[l:r]), longest)
                checking = False
        
        return longest