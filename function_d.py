def max_value(numbers):
    """ This function returns the largest number
        in the list.
    """
<<<<<<< HEAD
    max = numbers[0]
    for num in numbers:
        if num > max:
            max = num
    return max
=======
    result = []
    largest = 0
    for item in numbers:
        if item > largest:
            largest = item
    result.append(largest)
    return result
>>>>>>> 92fe02f7a8c8cfe59e1c77a7a5b05a67f8ab6f43


if __name__ == "__main__":
    print(max_value([1, 12, 2, 42, 8, 3]))
