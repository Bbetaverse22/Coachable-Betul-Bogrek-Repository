class Solution:
    """Solution Class"""

    def valid_ip_address(self, query_ip: str) -> str:
        """
        This function validates whether the given IP address is IPv4, IPv6, or neither.
        """
        def is_ipv4(ip: str) -> bool:
            parts = ip.split(".")
            if len(parts) != 4:
                return False
            for part in parts:
                if not part.isdigit() or not 0 <= int(part) <= 255 or (part[0] == '0' and len(part) > 1):
                    return False
            return True

        def is_ipv6(ip: str) -> bool:
            parts = ip.split(":")
            if len(parts) != 8:
                return False
            for part in parts:
                if not (1 <= len(part) <= 4) or not all(c in "0123456789abcdefABCDEF" for c in part):
                    return False
            return True

        if is_ipv4(query_ip):
            return "IPv4"
        elif is_ipv6(query_ip):
            return "IPv6"
        else:
            return "Neither"
