class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
       curr = sum(arr[:k])
       count = 0

       if curr >= k * threshold:
        count += 1

       for r in range(k, len(arr)):
        incoming_element = arr[r]
        outgoing_element = arr[r - k]

        curr = curr + (incoming_element - outgoing_element)

        if curr >= k * threshold:
            count += 1

       return count



       



                
