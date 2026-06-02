class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        original_s = {}

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            if s[i] not in original_s:
                original_s[s[i]] = 1
            else:
                original_s[s[i]] += 1
    

        for i in range(len(t)):
            if t[i] not in original_s:
                return False
            elif original_s[t[i]] - 1 < 0:
                return False
            else:
                original_s[t[i]] -= 1
        return True
        