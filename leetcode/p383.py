class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        hash_magazine = {}
        for char in magazine:
          if hash_magazine.get(char):
            hash_magazine[char] += 1
          else:
            hash_magazine[char] = 1
        for char in ransomNote:
          if not hash_magazine.get(char):
            return False
          hash_magazine[char] -= 1
          if hash_magazine[char] < 0:
            return False
        return True

solution = Solution()
ransomNote = "aa"
magazine = "b"
k = solution.canConstruct(ransomNote, magazine)
print(k)
