def check_palindrome(a: str):
    try:
        x = 0
        n = -1
        mid = len(a)//2
        while x < mid and n >= -mid:
            if a[x].lower() != a[n].lower():
                return "It is not a palindrome"
            x=x+1
            n = n-1
        return "It is a palindrome"
    except Exception as e:
        raise e


if __name__ == "__main__":
    a = input("Enter string to check palindrome:")
    result = check_palindrome(a)
    print(result)