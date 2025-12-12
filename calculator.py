def addition(a: float, b: float) -> float:
    try:
        result = a + b
    except TypeError:
        raise ValueError("Invalid input types for addition.")
    return result


def subtraction(a: float, b: float) -> float:
    try:
        result = a - b
    except TypeError:
        raise ValueError("Invalid input types for subtraction.")
    return result


def multiplication(a: float, b: float) -> float:
    try:
        result = a * b
    except TypeError:
        raise ValueError("Invalid input types for multiplication.")
    return result


def division(a: float, b: float) -> float:
    try:
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        result = a / b
    except TypeError:
        raise ValueError("Invalid input types for division.")
    return result


def power(a: float, b: float) -> float:
    try:
        result = a**b
    except TypeError:
        raise ValueError("Invalid input types for power operation.")
    return result


def square_root(a: float) -> float:
    try:
        if a < 0:
            raise ValueError("Cannot compute square root of a negative number.")
        result = a**0.5
    except TypeError:
        raise ValueError("Invalid input type for square root operation.")
    return result


def modulus(a: float, b: float) -> float:
    try:
        result = a % b
    except TypeError:
        raise ValueError("Invalid input types for modulus operation.")
    return result


def floor_division(a: float, b: float) -> float:
    try:
        if b == 0:
            raise ValueError("Cannot perform floor division by zero.")
        result = a // b
    except TypeError:
        raise ValueError("Invalid input types for floor division operation.")
    return result


def final_calculator(a, b):
    print("""
          Select operation:
                1. Addition
                2. Subtraction
                3. Multiplication
                4. Division
                5. Power
                6. Square Root
                7. Modulus
                8. Floor Division
          """
    )
def final_calculator():
    print("""
          Select operation:
                1. Addition
                2. Subtraction
                3. Multiplication
                4. Division
                5. Power
                6. Square Root
                7. Modulus
                8. Floor Division
          """
    )

    while True:
        try:
            # new numbers every iteration
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))

            n = int(input("Enter choice (1/2/3/4/5/6/7/8): "))

            if n == 1:
                print(f"{a} + {b} = {addition(a,b)}")
            elif n == 2:
                print(f"{a} - {b} = {subtraction(a,b)}")
            elif n == 3:
                print(f"{a} * {b} = {multiplication(a,b)}")
            elif n == 4:
                print(f"{a} / {b} = {division(a,b)}")
            elif n == 5:
                print(f"{a} ^ {b} = {power(a,b)}")
            elif n == 6:
                print(f"Square root of {a} = {square_root(a)}")
            elif n == 7:
                print(f"{a} % {b} = {modulus(a,b)}")
            elif n == 8:
                print(f"{a} // {b} = {floor_division(a,b)}")
            else:
                print("Invalid input")

        except ValueError as ve:
            print(ve)

        next_calculation = input("Do you want to perform another calculation? (yes/no): ")

        if next_calculation.lower() != "yes":
            break

if __name__ == "__main__":

    try:
        final_calculator()
    except ValueError:
        print("Invalid input. Please enter numeric values.")
