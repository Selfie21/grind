class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return None
        
        if len(nums1) == n:
            for i in range(n):
                nums1[i] = nums2[i]
            nums1 = nums2
            return None
        
        i1 = m - 1
        i2 = n - 1
        while i1 >= 0 and i2 >= 0:
            if nums1[i1] > nums2[i2]:
                nums1[i1 + i2 + 1] = nums1[i1]
                i1 -= 1
            else:
                nums1[i1 + i2 + 1] = nums2[i2]
                i2 -= 1
            
            # case nums1 all in order insert nums2
            if i1 < 0 and i2 >= 0:
                for i in range(i2, -1, -1):
                    nums1[i1 + i + 1] = nums2[i]
        print(nums1)

solution = Solution()
solution.merge([4,5,6,0,0,0], 3, [1,2,3], 3)