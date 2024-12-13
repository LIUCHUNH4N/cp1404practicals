"""
CP1404/CP5632 Practical
Test Silver Service Taxi
"""
from silver_service_taxi import SilverServiceTaxi


def main():
    """Test the SilverServiceTaxi class."""
    taxi = SilverServiceTaxi("Hummer", 200, 2)
    taxi.start_fare()
    taxi.drive(18)
    fare = taxi.get_fare()
    expected_fare = 48.80  # 4.50 (flagfall) + 18 * 2 * 1.23 (price_per_km with fanciness)
    assert fare == expected_fare, f"Expected fare: ${expected_fare:.2f}, but got ${fare:.2f}"
    print(f"Test passed! Fare: ${fare:.2f}")


if __name__ == "__main__":
    main()
