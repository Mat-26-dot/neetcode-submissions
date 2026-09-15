class MinStack:

    def __init__(self):
        self.main_stack = []
        self.min_stack = []
        # initialize empty stacks
    def push(self, val: int) -> None:
        self.main_stack.append(val)
        val = min(val, self.min_stack[-1] if self.min_stack else val)
           # compare value with current min or whichever is smallest
        self.min_stack.append(val)
        # push values onto both stacks if min is empty then push val

    def pop(self) -> None:
        self.main_stack.pop()
        self.min_stack.pop()
        # to keep the 2 stacks aligned
    def top(self) -> int:
        return self.main_stack[-1] 
        # here we are checking the number on top of stack and return and compare with min
    def getMin(self) -> int:
        return self.min_stack[-1]  
        #if lower num lower than main return if correct

'''2 empty stacks
      ↓
push values
      ↓
main_stack = stores everything
min_stack  = tracks minimums
      ↓
new value comes in
      ↓
compare it with current minimum
      ↓
update min_stack if needed
      ↓
POP → keep the stacks aligned
      ↓
top() → look at the top
getMin() → look at the minimum stack'''