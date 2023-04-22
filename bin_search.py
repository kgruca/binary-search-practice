def binary_search(list, value):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high) // 2
        attempt = list[mid]

        if attempt == value:
            return mid
        elif attempt > value:
            high = mid - 1
        else:
            low = mid + 1

    return None


new_list = ["as", "fgd", "gti", "h", "itwe", "klw"]

print(binary_search(new_list, "fgd"))
