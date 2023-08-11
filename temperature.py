def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def main():
    while True:
        print("Temperature Converter")
        print("1. Fahrenheit to Celsius")
        print("2. Celsius to Fahrenheit")
        print("3. Quit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
            celsius = fahrenheit_to_celsius(fahrenheit)
            print(f"{fahrenheit} Fahrenheit is equal to {celsius:.2f} Celsius.\n")

        elif choice == '2':
            celsius = float(input("Enter the temperature in Celsius: "))
            fahrenheit = celsius_to_fahrenheit(celsius)
            print(f"{celsius} Celsius is equal to {fahrenheit:.2f} Fahrenheit.\n")

        elif choice == '3':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a valid option.\n")

if __name__ == "__main__":
    main()
