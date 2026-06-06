class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                sum = nums[i] + nums[j] + nums[k]
                if sum == 0:
                    if [nums[i],nums[j],nums[k]] not in res:
                        res.append([nums[i],nums[j],nums[k]])
                    j += 1
                elif sum < 0:
                    j += 1
                else:
                    k -= 1
                
        return res

