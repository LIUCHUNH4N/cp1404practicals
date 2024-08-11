"""
CP1404/CP5632 Practical
Test Unreliable Car
"""
from unreliable_car import UnreliableCar


def main():
    # Create a new unreliable car object with 50% reliability
    car = UnreliableCar("Test Car", 100, 50)

    # Attempt to test 10 cars
    for i in range(10):
        success = car.drive(1)
        if success:
            print(f"Car {i + 1}: This is a reliable car!")
        else:
            print(f"Car {i + 1}: This is an unreliable car!")


if __name__ == "__main__":
    main()
