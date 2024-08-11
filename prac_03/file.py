# TASK 1
name = input("Enter your name: ")

name_file = open('name.txt', 'w')

name_file.write(name)

name_file.close()

# TASK 2
name_file = open('name.txt', 'r')

name_from_file = name_file.read().strip()

name_file.close()

print(f"Hi {name_from_file}!")

# TASK 3
with open('numbers.txt', 'r') as numbers_file:
    first_number = int(numbers_file.readline().strip())
    second_number = int(numbers_file.readline().strip())

result = first_number + second_number
print(result)

# TASK 4
total = 0
with open('numbers.txt', 'r') as numbers_file:
    for line in numbers_file:
        total += int(line.strip())

print(total)
