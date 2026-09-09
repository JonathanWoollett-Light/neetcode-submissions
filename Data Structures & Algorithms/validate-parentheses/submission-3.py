class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        cond = lambda a : (a != stack.pop()) if stack else True
        for c in s:
            match c:
                case '{' | '[' | '(':
                    stack.append(c)
                case '}':
                    if cond('{'):
                        return False
                case ']':
                    if cond('['):
                        return False
                case ')':
                    if cond('('):
                        return False
                case _:
                    pass
        return len(stack) == 0