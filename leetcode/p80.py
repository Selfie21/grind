class Solution(object):
	def removeDuplicates(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		move_index = 1
		unique_counter = 1
		unique = nums[0]
		for i in range(1, len(nums)):
			if nums[i] == unique and unique_counter < 2:
				nums[move_index] = nums[i]
				move_index += 1
				unique_counter += 1
			elif nums[i] != unique:
				nums[move_index] = nums[i]
				unique = nums[i]
				unique_counter = 1
				move_index += 1
			else:
				unique_counter += 1
		
		return move_index 

nums = [0,0,1,1,1,1,2,3,3] 
solution = Solution()
k = solution.removeDuplicates(nums)
print(k)
print(nums[:k])
