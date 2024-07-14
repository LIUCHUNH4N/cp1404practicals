"""
CP1404/CP5632 Practical
Playing the Guitars
Estimate: 50 minutes
Actual:   65 minutes
"""
from guitar import Guitar


def run_tests():
    # Test 1: Create a guitar instance and check its attributes
    guitar = Guitar("Gibson L-5 CES", 1922, 16035.40)
    print(guitar)
    print(f"Age: {guitar.get_age()}")
    print(f"Is vintage: {guitar.is_vintage()}")

    # Test 2: Create another guitar instance and check its attributes
    guitar2 = Guitar("Line 6 JTV-59", 2010, 1512.9)
    print(guitar2)
    print(f"Age: {guitar2.get_age()}")
    print(f"Is vintage: {guitar2.is_vintage()}")


run_tests()
