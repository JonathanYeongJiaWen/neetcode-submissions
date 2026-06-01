class Solution:
    def search(self, nums: List[int], target: int) -> int:
        s = 0
        e = len(nums)-1
        while s<=e:
            midP = (s+e)//2
            if target == nums[midP]:
                return midP
            elif target < nums[midP]:
                e = midP - 1
            else:
                s = midP + 1
        return -1
        