class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        hashset = set() # sort values in ascending order

        for n in nums: # loop value in array
            if n in hashset: # is value n stored already in hashset?
                return True
            hashset.add(n) # if array doesnt contain dup we add value
        return False


             



        