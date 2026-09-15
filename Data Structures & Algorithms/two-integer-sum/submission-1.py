class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # Empty hashmap to store index : value as we loop
        seen = {}
        # inserted loop to loop over index : value
        for i, n in enumerate(nums):
            # created var for target value
            diff = target - n
            # so if target value in hashmap equals index then ret value
            if diff in seen:
                return [seen[diff], i]
            # Update hashmap value n the index is i
            seen[n] = i