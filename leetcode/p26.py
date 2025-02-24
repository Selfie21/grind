class Solution(object):
	def removeDuplicates(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		unique_index = 1
		unique = nums[0]
		for i in range(len(nums)):
			if nums[i] != unique:
				nums[unique_index] = nums[i]
				unique_index += 1
				unique = nums[i]
		return unique_index
duplicates = [0,0,1,1,2,2,3,3,4,4]
solution = Solution()
k = solution.removeDuplicates(duplicates)
print(k)
