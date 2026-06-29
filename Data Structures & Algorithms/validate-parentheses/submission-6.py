class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parantheses_dict = {
            "(": ")",
            "{": "}",
            "[": "]"
        }
        
        for char in s:
            if char in parantheses_dict:
                stack.append(char)
            else:
                if not stack or parantheses_dict[stack.pop()] != char:
                    return False

        return not stack

        
            