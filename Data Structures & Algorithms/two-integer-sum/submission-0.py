class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {} # hashmap: index -> value 
        
        for i, num in enumerate(nums):
            cmpl = target - num
            if cmpl in hashmap:
                return [hashmap[cmpl], i]
            hashmap[num] = i

        