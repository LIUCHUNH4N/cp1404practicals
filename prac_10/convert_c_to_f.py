from flask import Flask

app = Flask(__name__)


# Copy the conversion function from temperatures.py
def convert_celsius_to_fahrenheit(celsius):
    return celsius * 9.0 / 5 + 32


@app.route('/f/<celsius>')
def show_fahrenheit(celsius):
    try:
        # Convert the Celsius value from the URL to a float
        celsius = float(celsius)
        fahrenheit = convert_celsius_to_fahrenheit(celsius)
        return f"{celsius} degrees Celsius is {fahrenheit:.2f} degrees Fahrenheit"
    except ValueError:
        return "Invalid input. Please enter a valid number for Celsius."


if __name__ == '__main__':
    app.run(debug=True)
