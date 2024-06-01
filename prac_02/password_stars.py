MIN_LENGTH = 8

password = input("Enter your password: ")
while len(password) < MIN_LENGTH:
    print(f"Password must be at least 8 characters long. Please try again.")
    password = input("Enter your password: ")
print('*' * len(password))