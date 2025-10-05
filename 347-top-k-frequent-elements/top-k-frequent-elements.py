class Solution:

    # O(N + klog n) time complexity => build up freq table + heapify k times 
    # O(N) space => 

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        nums_dict = {}

        # similar to bucket we need to store the freq of each num in nums
        for num in nums:
            nums_dict[num] = nums_dict.get(num, 0) + 1

        # Create a max_heap 
        # in python, heapq lib implements as a min-heap
        # we can create a put a negative sign in order to create a max heap
        # heapify uses the first element of each node so we need to put
        # frequency as first element 

        max_heap = [(-freq, num) for num, freq in nums_dict.items()]
        heapq.heapify(max_heap)

        res = []
        # heappop will help you to reheapify each time when you pop
        # an element from the heap
        for _ in range(k):
            res.append(heapq.heappop(max_heap)[1])
            
        return res

