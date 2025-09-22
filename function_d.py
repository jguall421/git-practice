def max_value(numbers):
    max = numbers[0]
    for number in numbers:
        if number > max:
            max = number

    return max
    """ This function returns the largest number
        in the list.
    """
    max = numbers[0]
    for num in numbers:
        if num > max:
            max = num
    return max
    result = []
    largest = 0
    for item in numbers:
        if item > largest:
            largest = item
    result.append(largest)
    return result


if __name__ == "__main__":
    print(max_value([1, 12, 2, 42, 8, 3]))
