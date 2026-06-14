class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 1:
            return nums
        count = defaultdict(int)
        freq = [[] for i in range(len(nums)+1)]
        res = []
        for n in nums:
            count[n] += 1
        for num, cnt in count.items():
            freq[cnt].append(num)
        for i in range(len(nums),0,-1):
            for number in freq[i]:
                res.append(number)
                if len(res) == k:
                    return res
        return res
        