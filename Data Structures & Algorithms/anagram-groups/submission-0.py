class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hashmap = {}

        for word in strs: # outer loop, iterate over each word in strs
            count = [0] * 26
            
            for char in word: #inner loop, iterate over each word in char in word
                index = ord(char) - ord('a') 
                count[index] = count[index] + 1
            key = tuple(count)
            hashmap.setdefault(key, []).append(word)
        
        return list(hashmap.values())
        
        
    '''my thinking is: if i use an empty dictionary and iterate throught 
        the list and generate a unique char sinature, use the unique 
        signature as the key, append the word list and return all hashmap values
        
        - create an empty hash to store word count
        - loop for looping over each word in strs
        - create a unique sinature for containing 26 zeros
        - loop for each char in word
        - find its index via ascii
        - increment [index] count by 1
        - convert count to tuple
        - use .setdefault(key, [] then append word to it
        - then out of the loop we'll return list(hashmap.values())'''

