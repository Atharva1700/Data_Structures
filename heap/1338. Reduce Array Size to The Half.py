from collections import Counter
import heapq

class Solution(object):
    def minSetSize(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        counter = Counter(arr)
        n = len(arr) // 2
        i = 0
        store_f = 0
        heap_max = []

        for char, freq in counter.items():
            heapq.heappush(heap_max, (-freq, char))

        while store_f < n:
            freq, char = heapq.heappop(heap_max)
            i += 1
            store_f = store_f - freq  # because freq is negative
        return i

# Main function
if __name__ == "__main__":
    arr = [3,3,3,3,5,5,5,2,2,7]
    sol = Solution()
    result = sol.minSetSize(arr)
    print("Minimum set size to remove at least half of the array:", result)
