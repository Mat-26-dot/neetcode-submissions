class Solution(object):
    def hasDuplicate(self, nums: List[int]) -> bool:     
        # because hashsets only take in unique numbers the duplicate is ignored so this does not equal the length of the array therefore a duplicate is present then we return true
        return len(set(nums)) != len(nums)


# Another solution is - 
        # seen = set()
        # loop through array - (for num in nums:)
        # then we check for early release if dup is found and the rest of the code ignored
        # if not then otherwise we add 'seen' to num - seen.add(num)
        # then we return false to handle if no dups were found - return false