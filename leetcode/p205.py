class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if len(s) != len(t):
            return False
        mapping = {}
        for i in range(len(s)):
            if mapping.get(s[i]):
                if mapping[s[i]] != t[i]:
                    return False
                else: continue
            if t[i] in mapping.values():
                return False
            mapping[s[i]] = t[i]
        return True


s = "add"
t = "egg"
solution = Solution()
k = solution.isIsomorphic(s, t)
print(k)