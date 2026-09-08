class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_dict = {} # create empty dictionary
        res = []

        for i in nums: # create the frequency count for each integer in the dictionary
            nums_dict[i] = nums_dict.get(i, 0) + 1 
        
        nums_dict = dict(sorted(nums_dict.items(), key = lambda x:x[1], reverse = True)) # Sort the dictionary in descending order of value
        for i,v in nums_dict.items(): # iterate through the dictionary and pick first k keys
            if k > 0:
                res.append(i) # append the key in the res variable
                k -= 1
            else:
                break # break out of loop as soon as k goes to 0
        
        return res
            


