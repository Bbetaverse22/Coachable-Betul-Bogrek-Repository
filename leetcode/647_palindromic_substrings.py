"""647. Palindromic Substrings"""

def countSubstrings(s: str) -> int:
    """
    Count the number of palindromic substrings in the input string.
    """
    n = len(s)
    count = 0

    def expandAroundCenter(left: int, right: int) -> int:
        nonlocal count
        while left >= 0 and right < n and s[left] == s[right]:
            count += 1
            left -= 1
            right += 1
    
    for i in range(n):
        expandAroundCenter(i, i)
        expandAroundCenter(i, i + 1)
    
    return count
