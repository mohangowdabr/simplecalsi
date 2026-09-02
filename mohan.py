import math

def calculate_square_root():
    try:
        value = float(input("Enter a non-negative number: "))
        if value < 0:
            print("Cannot calculate square root of a negative number.")
            return
        result = math.sqrt(value)
        print(f"Square root of {value} is {result}")
    except ValueError:
        print("Invalid input. Please enter a correct one.")

if __name__ == "__main__":
    calculate_square_root()

# meow meow
#green green

