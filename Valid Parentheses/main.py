class Stack:
    def __init__(self, str_ = []) -> None:
        self.stack = [c for c in str_]

    def push(self, value):
        self.stack.append(value)

    def empty(self):
        return len(self.stack) == 0

    def top(self):
        return self.stack[-1]

    def pop(self):
        self.stack.pop()


class Solution:
    def isValid(self, s: str) -> bool:
        main_stack = Stack(s)
        aux_stack = Stack()
        
        while not main_stack.empty():
            main_stack_top = main_stack.top()
        
            if aux_stack.empty():
                aux_stack.push(main_stack_top)
                main_stack.pop()
                continue
        
            aux_stack_top = aux_stack.top()
            if main_stack_top == "(" and aux_stack_top == ")" or main_stack_top == "{" and aux_stack_top == "}" or main_stack_top == "[" and aux_stack_top == "]":
                main_stack.pop()
                aux_stack.pop()
                continue

            aux_stack.push(main_stack_top)
            main_stack.pop()
            
        if main_stack.empty() and aux_stack.empty():
            return True

        return False

result = Solution().isValid("()")
print(f" () ---> {result}")

result = Solution().isValid("()[]{}")
print(" ()[]{} ---> " + str(result))

result = Solution().isValid("(]")
print(f" (] ---> {result}")

result = Solution().isValid("(({}))")
print(" (({})) ---> "+ str(result))




