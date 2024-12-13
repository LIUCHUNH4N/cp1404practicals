"""
CP1404/CP5632 Practical
More Guitars!
Estimate: 50 minutes
Actual:   65 minutes
"""


class Guitar:

    def __init__(self, name, year, cost):
        self.name = name
        self.year = year
        self.cost = cost

    def get_age(self):
        current_year = 2024
        return current_year - self.year

    def is_vintage(self):
        return self.get_age() >= 50

    def __str__(self):
        return f"{self.name} ({self.year}), worth ${self.cost:.2f}"

    def __lt__(self, other):
        return self.year < other.year
