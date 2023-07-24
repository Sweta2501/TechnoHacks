a = input("Is this temperature in Celsius or Fahrenheit (C/F): ")
temperature = float(input("Enter the temperature: "))

if a == "C":
    temperature = round((9 * temperature) / 5 + 32, 1)
    print(f"Temperature in Fahrenheit is: {temperature}°F")
elif a == "F":
    temperature = round((temperature - 32) * 5 / 9, 1)
    print(f"Temperature in Celsius is: {temperature}°C")
else:
    print(f"{a} is an invalid unit of measurement")