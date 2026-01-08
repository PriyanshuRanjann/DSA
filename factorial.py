def get_factorial(n):
    try:
        if n < 0:
            return "Error: Factorial is not defined for negative numbers."
        elif n == 0 or n == 1:
            return 1
        else:
            return n * get_factorial(n - 1)
    except RecursionError as e:
        return e
    
if __name__ == "__main__":
    n = int(input("Enter a non-negative integer: "))
    result = get_factorial(n)
    print(f"The factorial of {n} is {result}")