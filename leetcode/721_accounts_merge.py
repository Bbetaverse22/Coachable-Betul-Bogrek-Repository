"""721 Accounts Merge"""
from typing import List
from collections import defaultdict

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        """
        Given a list of accounts where each account is a list of strings, this function merges the accounts.
        Each account contains a name and a list of emails. Two accounts are considered to be the same if they
        have at least one email in common. The function returns the merged accounts in the format [name, email1, email2, ...].
        """
        parent = {}
        email_to_name = {}
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                parent[rootY] = rootX
        
        # Initialize the union-find structure
        for account in accounts:
            name = account[0]
            for email in account[1:]:
                if email not in parent:
                    parent[email] = email
                email_to_name[email] = name
                union(account[1], email)
        
        # Group emails by their root parent
        merged_accounts = defaultdict(list)
        for email in parent:
            root = find(email)
            merged_accounts[root].append(email)
        
        # Format the result
        result = []
        for emails in merged_accounts.values():
            result.append([email_to_name[emails[0]]] + sorted(emails))
        
        return result
