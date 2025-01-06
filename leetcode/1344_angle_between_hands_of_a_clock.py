"""1344. Angle Between Hands of a Clock"""

class Solution:
    """Solution Class"""

    def angle_clock(self, hour: int, minutes: int) -> float:
        """
        This function calculates the angle between the hour and minute hands of a clock.
        """
        minute_angle = minutes * 6
        
        hour_angle = (hour % 12) * 30 + minutes * 0.5
        
        angle = abs(hour_angle - minute_angle)
        
        return min(angle, 360 - angle)
