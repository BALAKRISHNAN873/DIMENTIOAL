def get_number(prompt):
    """Safely get a float number from the user."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def main():
    print("Enter 4 numbers to add:")

    # Get 4 numbers from the user
    num1 = get_number("Number 1: ")
    num2 = get_number("Number 2: ")
    num3 = get_number("Number 3: ")
    num4 = get_number("Number 4: ")

    # Calculate the sum
    total = num1 + num2 + num3 + num4

    # Display the result
    print(f"The sum of {num1}, {num2}, {num3}, and {num4} is: {total}")

if __name__ == "__main__":
    main()
