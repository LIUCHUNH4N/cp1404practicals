"""
CP1404/CP5632 Practical
More Guitars!
Estimate: 50 minutes
Actual:   65 minutes
"""

from guitar import Guitar


def main():
    guitars = []

    # Read from the CSV file
    with open('guitars.csv', 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            name = parts[0]
            year = int(parts[1])
            cost = float(parts[2])
            guitars.append(Guitar(name, year, cost))

    # Display all guitars
    print("These are my guitars:")
    for guitar in guitars:
        print(guitar)

    # Sort guitars by year
    guitars.sort()

    # Display sorted guitars
    print("\nThese are my guitars sorted by year (oldest to newest):")
    for guitar in guitars:
        print(guitar)

    # Add new guitars
    while True:
        name = input("Enter guitar name (or 'q' to quit): ")
        if name.lower() == 'q':
            break
        year = int(input("Enter year: "))
        cost = float(input("Enter cost: "))
        guitars.append(Guitar(name, year, cost))

    # Write all guitars back to the CSV file
    with open('guitars.csv', 'w') as file:
        for guitar in guitars:
            file.write(f"{guitar.name},{guitar.year},{guitar.cost}\n")


if __name__ == "__main__":
    main()
