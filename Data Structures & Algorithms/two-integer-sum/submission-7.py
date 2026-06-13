class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idx = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in idx:
                # return [min(idx[complement], i), max(idx[complement], i)]
                return [idx[complement], i]
            idx[nums[i]] = i