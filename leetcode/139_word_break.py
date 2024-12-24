"""139. Word Break"""

class Solution:
    def wordBreak(s: str, wordDict: list) -> bool:
        """
        Given a string s and a dictionary of strings wordDict, return true
        if s can be segmented into a space-separated sequence of one or more dictionary words.
        """
        word_set = set(wordDict)
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break

        return dp[-1]
