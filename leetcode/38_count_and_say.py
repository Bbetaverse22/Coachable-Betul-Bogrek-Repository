class Solution:
    """Solution Class"""

    def count_and_say(self, n: int) -> str:
        """
        This function generates the nth term in the count-and-say sequence.
        """
        if n == 1:
            return "1"
        
        previous_term = self.count_and_say(n - 1)
        result = ""
        count = 1
        
        for i in range(1, len(previous_term)):
            if previous_term[i] == previous_term[i - 1]:
                count += 1
            else:
                result += str(count) + previous_term[i - 1]
                count = 1
        
        result += str(count) + previous_term[-1]
        return result
