"""
CP1404/CP5632 Practical
Colors in a dictionary
"""

COLOR_CODES = {
    "AliceBlue": "#f0f8ff",
    "AntiqueWhite": "#faebd7",
    "Aqua": "#00ffff",
    "Aquamarine": "#7fffd4",
    "Azure": "#f0ffff",
    "Beige": "#f5f5dc",
    "Bisque": "#ffe4c4",
    "Black": "#000000",
    "BlanchedAlmond": "#ffebcd",
    "Blue": "#0000ff"}

print(COLOR_CODES)

for name, code in COLOR_CODES.items():
    print(f"{name:<14} is {code}")

while True:
    color_name = input("Enter color name: ").strip().capitalize()
    if color_name == "":
        break
    try:
        print(color_name, "is", COLOR_CODES[color_name])
    except KeyError:
        print("Invalid color name")
