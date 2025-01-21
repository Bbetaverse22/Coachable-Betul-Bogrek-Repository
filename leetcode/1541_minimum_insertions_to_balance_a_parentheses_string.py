"""1541. Minimum Insertions to Balance a Parentheses String"""

class Solution:
    """Solution Class"""

    def minInsertions(self, s: str) -> int:
        """
        This function returns the minimum number of insertions needed
        to balance a parentheses string.
        """
        left_needed = 0
        right_needed = 0

        i = 0
        while i < len(s):
            if s[i] == '(':
                right_needed += 2
                if right_needed % 2 == 1:
                    left_needed += 1
                    right_needed -= 1
            else:
                right_needed -= 1
                if right_needed == -1:
                    left_needed += 1
                    right_needed = 1
            i += 1

        return left_needed + right_needed
