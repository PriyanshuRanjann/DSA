names = "animal,husbandary,fisheries!!!!!!! @#$%^&*()"


def take_n_char():
    try:
        n = int(input("Enter number of characters to extract: "))
        result = names[0:n]
    except Exception as e:
        print(f"An error occurred: {e}")
    return result


def len_of_string():
    try:
        result = len(names)
    except Exception as e:
        print(f"An error occurred: {e}")
    return result


def loop_in_string():
    try:
        for i in names:
            print(i)
    except Exception as e:
        print(f"An error occurred: {e}")


def string_methods():
    try:
        uppercase = names.upper()
    except Exception as e:
        print(f"An error occurred: {e}")
    try:
        lowercase = names.lower()
    except Exception as e:
        print(f"An error occurred: {e}")
    try:
        r_strip = names.rstrip("! @#$%^&*()")

    except Exception as e:
        print(f"An error occurred: {e}")
    try:
        x = input("Enter a name to be replaced by: ")
        replace = names.replace("animal", x)
    except Exception as e:
        print(f"An error occurred: {e}")
    try:
        split = names.split(" ")
    except Exception as e:
        print(f"An error occurred: {e}")
    try:
        split_comma = names.split(",")
    except Exception as e:
        print(f"An error occurred: {e}")
    try:
        string_to_count = input("Enter a substring to count its occurrences: ")
        count_occurrences = names.count(string_to_count)
    except Exception as e:
        print(f"An error occurred: {e}")
    result = {
        "uppercase": uppercase,
        "lowercase": lowercase,
        "r_strip": r_strip,
        "replace": replace,
        "split_by_space": split,
        "split_by_comma": split_comma,
        "count": count_occurrences,
    }
    return result


if __name__ == "__main__":
    print(take_n_char())
    print(len_of_string())
    # loop_in_string()
    print(string_methods())
