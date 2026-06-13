class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        store = defaultdict(int)
        freq = []
        for n in nums:
            store[n] += 1
        for key,v in store.items():
            freq.append((key,v))
        freq.sort(key = lambda x: x[1], reverse=True)
        res = []
        for i in range(k):
            res.append(freq[i][0])
        return res
        
        


        
