import random
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        unique = list(cnt.keys())

        def partition(left, right, pivot_index) -> int:
            pivot_frequency = cnt[unique[pivot_index]]
            # 1. Move the pivot to end
            unique[pivot_index], unique[right] = unique[right], unique[pivot_index]

            # 2. Move all less frequent elements to the left
            store_index = left
            for i in range(left, right):
                if cnt[unique[i]] < pivot_frequency:
                    unique[store_index], unique[i] = unique[i], unique[store_index]
                    store_index += 1
                
            # 3. Move the pivot to its final place
            unique[right], unique[store_index] = unique[store_index], unique[right]

            return store_index
        
        def quickselect(left, right, k_smallest) -> None:
            """
            Sort a list within left .. right till kth less frequent element takes its place
            """

            # base case: the list contains only one element
            if left == right:
                return 
            
            # Select a random pivot_index
            pivot_index = random.randint(left, right)

            # Find the pivot position in a sorted list
            pivot_index = partition(left, right, pivot_index)

            # If the pivot is in its final sorted position:
            if k_smallest == pivot_index:
                return
            # go left
            elif k_smallest < pivot_index:
                quickselect(left, pivot_index - 1, k_smallest)

            # go right
            else:
                quickselect(pivot_index + 1, right, k_smallest)

        n = len(unique)
        quickselect(0, n - 1, n - k)

        return unique[n-k:]