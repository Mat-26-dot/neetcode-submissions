class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashmap = {')': '(', '}': '{', ']': '['}

        for char in s: #scan input left and right
            if char in hashmap: # if contain opening bracket - push
                if not stack or stack[-1] != hashmap[char]:
                # if last item on stack not closing bracket 
                    return False
                stack.pop()

            else:
                stack.append(char)
        
        return len(stack) == 0








        '''if opening bracket in the string we append 
        - if closing bracket we pop
        - if brackets dont close in correct order we return invalid
        - otherwise true if whole stack is seen and is empty - valid'''