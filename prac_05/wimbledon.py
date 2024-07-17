"""
CP1404/CP5632 Practical
Game, Set, Match
Estimate: 40 minutes
Actual:   50 minutes
"""
import csv


def main():
    filename = 'wimbledon.csv'
    data = read_wimbledon_data(filename)

    champions_count = count_champions(data)
    countries = list_countries(data)

    print("Wimbledon Champions:")
    for champion, count in sorted(champions_count.items()):
        print(f"{champion} {count}")

    print(f"\nThese {len(countries)} countries have won Wimbledon:")
    print(", ".join(countries))


def read_wimbledon_data(filename):
    with open(filename, "r", encoding="utf-8-sig") as file:
        reader = csv.reader(file)
        return list(reader)


def count_champions(data):
    champions_count = {}
    for row in data:
        champion = row[2]
        if champion in champions_count:
            champions_count[champion] += 1
        else:
            champions_count[champion] = 1
    return champions_count


def list_countries(data):
    countries = set()
    for row in data:
        country = row[1]
        if country != "Country" and country != "":
            countries.add(country)
    return sorted(countries)


main()
