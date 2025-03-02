"""670. Maximum Swap"""

class Solution:
    def maximumSwap(self, num: int) -> int:
        """
        Given a non-negative integer, this function returns the maximum value
        that can be obtained by swapping two digits of the integer at most once.
        """
        num_list = list(str(num))
        last = {int(x): i for i, x in enumerate(num_list)}

        for i, x in enumerate(num_list):
            for d in range(9, int(x), -1):
                if last.get(d, -1) > i:
                    num_list[i], num_list[last[d]] = num_list[last[d]], num_list[i]
                    return int("".join(num_list))
        return num
