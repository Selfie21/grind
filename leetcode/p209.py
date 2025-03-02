class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        min = len(nums) + 1
        total = nums[0]
        start = 0
        end = 1
        while start < len(nums) and end <= len(nums):
            total += start
            if total >= target:
                if min > (end - start):
                    min = end - start
                start += 1
            end += 1
        if min == len(nums) + 1:
            return 0
        return min
target = 7
nums = [2,3,1,2,4,3]
solution = Solution()
k = solution.minSubArrayLen(target, nums)
print(k)