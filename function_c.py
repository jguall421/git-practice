def merge_lists(list_a, list_b):
    result = []
    for item in list_a:
        if item not in result:
            result.append(item)
    for item in list_b:
        if item not in result:
            result.append(item)
    return result


if __name__ == "__main__":
    print(merge_lists([1, 1, 2, 3], [3, 4, 5]))
