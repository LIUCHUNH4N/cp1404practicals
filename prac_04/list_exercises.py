"""
CP1404/CP5632 Practical
Basic list operations and Woefully inadequate security checker
"""


def main():
    numbers = get_numbers()
    display_number_info(numbers)
    check_username()


def get_numbers():
    numbers = []
    for i in range(5):
        number = float(input(f"Number {i + 1}: "))
        numbers.append(number)
    return numbers


def display_number_info(numbers):
    print(f"The first number is {numbers[0]}")
    print(f"The last number is {numbers[-1]}")
    print(f"The smallest number is {min(numbers)}")
    print(f"The largest number is {max(numbers)}")
    print(f"The average of the numbers is {sum(numbers) / len(numbers)}")


def check_username():
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicoleEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
    username = input("Enter your username: ")
    if username in usernames:
        print("Access granted")
    else:
        print("Access denied")


main()
