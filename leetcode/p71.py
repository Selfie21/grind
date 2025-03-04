class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []
        elements = path.split("/")
        for element in elements:
          if element == "":
            continue
          elif element == ".":
            continue
          elif element == "..":
            if len(stack) > 0:
              stack.pop()
          else:
            stack.append(element)

        if not stack:
          return "/"
        else:
          canonical_path = ""
          for element in stack:
            canonical_path += f"/{element}"
          return canonical_path

path = "/home/user/Documents/../Pictures"
solution = Solution()
k = solution.simplifyPath(path)
print(k)
