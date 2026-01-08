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

def fibonacci_recursion(n):
    try:
        a=0
        b=1
        if n <=0:
            return []
        elif n == 1:
            return [a]
        elif n == 2:
            return [a, b]
        else:
            lst = fibonacci_recursion(n - 1)
            lst.append(lst[-1] + lst[-2])
            return lst
    except RecursionError as e:
        return e

if __name__ == "__main__":
    num = int(input("Enter the number of terms in Fibonacci sequence: "))
    print(f"Fibonacci sequence with {num} terms: {fibonacci_recursion(num)}")
