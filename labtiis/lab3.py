import random


# Generate random temperature readings
def generate_temperature_data():
    # Set the temperature range in Celsius
    min_temperature = 18
    max_temperature = 30

    # Generate a random temperature reading within the range
    temperature = random.uniform(min_temperature, max_temperature)

    # Convert temperature to Fahrenheit
    temperature_f = (temperature * 9 / 5) + 32

    return temperature_f


# Generate 10 temperature readings
for i in range(10):
    temperature = generate_temperature_data()
    print("Temperature reading", i + 1, ":", temperature, "°F")
