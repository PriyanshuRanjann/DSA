def fibonacci(n: int):
    lst = []
    try:
        a, b = 0, 1
        while len(lst) < n:
            lst.append(a)
            a, b = b, a + b
    except Exception as e:
        print(f"An error occurred: {e}")
    return lst


if __name__ == "__main__":
    num = int(input("Enter the number of terms in Fibonacci sequence: "))
    print(f"Fibonacci sequence with {num} terms: {fibonacci(num)}")
