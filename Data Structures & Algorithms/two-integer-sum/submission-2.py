class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} # 1

        for i, n in enumerate(nums): #2 
            diff = target - n # 
            if diff in seen: #4
                return [seen[diff], i]
            seen[n] = i #5
        
        '''
        - start iterating at index 0 with value 2
        - calculate diff 9 - 2 = 7
        - check if 7 is in seen - its not
        - store 2[n] in seen
                
                2 Iteration
        
        - move to index 1 with value 7
        - calculate diff - 9 - 2 = 7
        - check if 2 is in seen - it is!
        - found pair! Return [0, 1]'''

        
        
        '''we create empty dict to store numbers seen

        loop through index and value using built in fun to return index an value

        create var with target and n and we pass through the var

        then we check if the target and index has already been found in the dict and we return

        then we assign the dict with the index and value'''

