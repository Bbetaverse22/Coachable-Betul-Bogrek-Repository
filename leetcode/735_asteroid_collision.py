"""Asteroid Collision"""
from typing import List

class Solution:

    def asteroid_collision(self, asteroids: List[int]) -> List[int]:
        """
        Simulates the collision of asteroids coming from left to right.
        """
        stack = []
        for ast in asteroids:
            while stack and ast < 0 < stack[-1]:
                if stack[-1] < -ast:
                    stack.pop()
                    continue
                if stack[-1] == -ast:
                    stack.pop()
                break
            else:
                stack.append(ast)
        return stack
