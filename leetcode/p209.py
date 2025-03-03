class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        minimum = float("inf")
        end = 0
        sum = nums[end]
        for start in range(len(nums)):
            while sum < target:
                if end + 1 >= len(nums):
                    break
                else:
                    end += 1
                sum += nums[end]
            if sum >= target:
                tmp_min = (end - start) + 1
                if tmp_min < minimum:
                    minimum = tmp_min
            sum -= nums[start]
        if minimum == float("inf"):
            return 0
        else:
            return minimum
target = 7
nums = [1,7,4]
solution = Solution()
k = solution.minSubArrayLen(target, nums)
print(k)