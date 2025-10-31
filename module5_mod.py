"""
Handinlg data initialization, insertion, and search using OOP.
"""

class NumberCollection:
    def __init__(self, capacity=None):
        """Initialize the collection (optionally with a capacity hint)."""
        self.capacity = capacity
        self.numbers = []

    def insert_number(self, num: int):
        """Insert one number into the collection."""
        self.numbers.append(num)

    def find_number(self, x: int) -> int:
        """
        Return 1-based index of the first occurrence of x.
        Return -1 if x is not found.
        """
        if x in self.numbers:
            return self.numbers.index(x) + 1
        else:
            return -1
