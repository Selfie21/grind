class Solution(object):
	def removeElement(self, nums, val):
		"""
		:type nums: List[int]
		:type val: int
		:rtype: int
		"""

		k = 0
		val_places = []
		for i in range(len(nums)):
			if nums[i] == val:
				val_places.append(i)
			else:
				k += 1
		
		while len(val_places) > 0 and i > 0:
			if nums[i] != val:
				tmp = val_places.pop(0)
				nums[tmp] = nums[i]
			i -= 1
		return k

nums = [3,2,2,3]
val = 3
solution = Solution()
solution.removeElement(nums, val)
