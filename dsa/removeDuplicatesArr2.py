#80. Remove Duplicates from Sorted Array II

class removeDuplicatesArr2(object):
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        if len(nums)<=2:
            return len(nums)

        slow = 2

        for fast in range(2,len(nums)):
           if nums[fast] != nums[slow-2] :
                 nums[slow] = nums[fast]
                 slow +=1
        return slow