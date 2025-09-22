def max_value(numbers):
    max = numbers[0]
    for number in numbers:
        if number > max:
            max = number

    return max


if __name__ == "__main__":
    print(max_value([1, 12, 2, 42, 8, 3]))
