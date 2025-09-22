def max_value(numbers):
    """ This function returns the largest number
        in the list.
    """
    result = []
    largest = 0
    for item in numbers:
        if item > largest:
            largest = item
    result.append(largest)
    return result


if __name__ == "__main__":
    print(max_value([1, 12, 2, 42, 8, 3]))
