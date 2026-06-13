class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        store = defaultdict(int)
        for n in nums:
            store[n] += 1
        freqL = [[] for _ in range(len(nums)+1)]
        for num, frequency in store.items():
            freqL[frequency].append(num)
        res = []
        for i in range(len(nums),0,-1):
            for num in freqL[i]:
                res.append(num)
            if len(res) == k:
                return res

