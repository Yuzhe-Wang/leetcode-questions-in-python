class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 1
        while i > 0:
            if nums[i] <= nums[i-1]:
                i -= 1
                continue
            else:
                j = i - 1
                k = i
                while k < len(nums) and nums[k] > nums[j]:
                    k +=1
                temp = nums[k-1]
                nums[k-1] = nums[j]
                nums[j] = temp
                nums[j+1:len(nums)] = sorted(nums[j+1:len(nums)])
                return nums
        return nums.sort()
                    
                    
                    
'''
starting from the back, traverse until the previous number is less than the current number
then find then closest number in the traversed part of the list
exchange them, sort and append the rest of the traversed part
61432

'''