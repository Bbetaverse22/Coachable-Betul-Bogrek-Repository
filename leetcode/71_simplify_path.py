"""71. Simplify Path"""

class Solution:
    def simplify_path(self, path: str) -> str:
        """Simplify the given Unix-style file path."""
        path_parts = path.split('/')
        result = []
        for part in path_parts:
            if part == '..':
                if result:
                    result.pop()
            elif part and part != ".":
                result.append(part)
        return '/' + '/'.join(result)
