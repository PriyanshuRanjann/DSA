"""
Given an integer n, for every positive integer i <= n, the task is to print,
    - "FizzBuzz" if i is divisible by 3 and 5,
    - "Fizz" if i is divisible by 3,
    - "Buzz" if i is divisible by 5
    - "i" as a string, if none of the conditions are true.
"""
def fizzbuzz(lst: list):
    try:
        for i in range (len(lst)):
            if lst[i] % 3 == 0 and lst[i] % 5 != 0 :
                lst[i] = "fizz"
            elif lst[i] % 5 == 0 and lst[i] % 3 != 0 :
                lst[i] = "Buzz"
            elif  lst[i] % 5 == 0 and lst[i] % 3 == 0 :
                lst[i] = "FizzBuzz"
            else:
                continue
    except Exception as e:
        raise e
    return lst

if __name__=="__main__":
    lst = eval(input("Enter array of integers:"))
    result = fizzbuzz(lst)
    print(result)