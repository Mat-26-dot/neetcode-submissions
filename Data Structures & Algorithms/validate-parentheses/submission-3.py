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


    '''See opening bracket --> append onto stack
       See closing bracket --> pop if top matches, else invalid
       Stack empty but closing bracket --> invalid
       Scan done, empty stack - valid'''