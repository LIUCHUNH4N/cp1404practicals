"""
CP1404/CP5632 Practical
Band Class
"""


class Band:
    """Band class that contains a list of musicians."""

    def __init__(self, name):
        """Initialize the Band with a name and an empty list of musicians."""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return a string representation of the Band."""
        return f"{self.name} ({', '.join(str(musician) for musician in self.musicians)})"

    def add(self, musician):
        """Add a musician to the band."""
        self.musicians.append(musician)

    def play(self):
        """Return a string showing each musician playing their instrument, or needing one."""
        return "\n".join(musician.play() for musician in self.musicians)
