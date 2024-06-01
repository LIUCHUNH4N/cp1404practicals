"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

import random


def main():
    score = float(input("Enter score: "))
    result = determine_result(score)
    print(result)

    random_score = random.uniform(0, 100)
    random_result = determine_result(random_score)
    print(f"Random score: {random_score:.2f}")
    print(random_result)


def determine_result(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score > 90:
        return "Excellent"
    elif score > 50:
        return "Passable"
    else:
        return "Bad"


main()
