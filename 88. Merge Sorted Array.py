class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        curr = m + n - 1
        left = m - 1
        right = n - 1
        
        # merge backwards
        while left >=0 and right >= 0:
            if nums1[left] >= nums2[right]:
                nums1[curr] = nums1[left]
                left -= 1
            else:
                nums1[curr] = nums2[right]
                right -= 1
            curr -= 1
        
        while right >= 0:
            nums1[curr] = nums2[right]
            curr -= 1
            right -= 1
        return