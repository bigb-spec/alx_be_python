#global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
       
def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    try:
        #prompt user to enter temperature
        temp_input = float(input("Enter the temperature to convert: "))
        #prompt to ask user to specify the unit
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")
        
        if unit == 'F':
            celsius = convert_to_celsius(temp_input)
            print(f"{temp_input} °F is {celsius} °C")
        elif unit == 'C':
            fahrenheit = convert_to_fahrenheit(temp_input)
            print(f"{temp_input} °C is {fahrenheit} °F")
        else:
            print("Invalid input. Please enter 'C' or 'F' for the unit")
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    main()