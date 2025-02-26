class Solution(object):
		def majorityElement(self, nums):
			"""
			:type nums: List[int]
			:rtype: int
			"""
			counter = {}
			majority = int(len(nums) / 2)
			for num in nums:
				if counter.get(num):
					counter[num] += 1
				else:
					counter[num] = 1
				if counter[num] > majority:
					return num 

nums = [3,2,3]
solution = Solution()
k = solution.majorityElement(nums)
print(k)
