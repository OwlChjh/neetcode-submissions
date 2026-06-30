class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = {}
        heap = []
        res = []
        for num in nums:
            if num not in cnt:
                cnt[num] = 1
            cnt[num] += 1
        
        for key in cnt:
            heapq.heappush(heap, (-cnt[key], key))
        
        for i in range(k):
            priority , value = heapq.heappop(heap)
            res.append(value)

        return res