"""Remove Sub-Folders"""
from typing import List

class Solution:

    def remove_subfolders(self, folder: List[str]) -> List[str]:
        """
        Removes sub-folders from the given list so that no folder is a sub-folder of another.
         """
        folder.sort()
        result = []
        for f in folder:
            if not result or not f.startswith(result[-1] + "/"):
                result.append(f)
        return result
