"""921 Minimum Add to Make Parentheses Valid"""
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        """Find the minimum number of parentheses needed to make the string valid."""
        left_bracket = 0
        right_bracket = 0

        for char in s:
            if char == '(':
                left_bracket += 1
            elif char == ')':
                if left_bracket > 0:
                    left_bracket -= 1
                else:
                    right_bracket += 1

        return left_bracket + right_bracket
