class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        countS, countT = {}, {}

        for i in range(len(s)):
        # Get current count -> add 1 -> add to dictionary. (0) means default
            countS[s[i]] = countS.get(s[i], 0) + 1
            countT[t[i]] = countT.get(t[i], 0) + 1
            
                       
        return countS == countT
 
       
        ''' P - if both string contain same frequencies forwards and backwards 
        they are an anogram 

        E - input: S = 'racecar', t = 'carrace'
        Output: True
        input: s = 'jar', t = 'jam'
        Output False

        D - Hashmap

        A - 1. We check to see to compare the length of both strings for 
        an early edge case and code will then return without 
        checking following code and just return boolean

        2. Then we create empty hashmaps for each string to store 
        char frequencies for each string
        
        3. We create counters for each string (s, t) and iterate by 1 
        starting both strings from index - increase char counter for s[i] 
        and second map t[i] using .get
        
        4. Finally we return and compare both strings

        C - Code up!'''

