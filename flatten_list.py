def flattened_list(lst: list):
    result = []
    try:
        for i in lst:
            if type(i) != list:
                result.append(i)
            else:
                result.extend(flattened_list(i))
    except Exception as e:
        print(f"An error occurred: {e}")
    return result


if __name__ == "__main__":
    nested_list = input("Enter a nested list (e.g., [1, [2, 3], 4]): ")
    result = flattened_list(eval(nested_list))
    print(f"Flattened list: {result}")