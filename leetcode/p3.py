class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        k = 0
        for i in range(len(s)):
          unique = set()
          tmp_k = 0
          while i < len(s) and s[i] not in unique:
            tmp_k += 1
            unique.add(s[i])
            i += 1
          if tmp_k > k:
            k = tmp_k
        return k

s = "pwwkew"
solution = Solution()
k = solution.lengthOfLongestSubstring(s)
print(k)
