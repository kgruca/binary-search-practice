# def binary_search(list, value):
#     low = 0
#     high = len(list) - 1

#     while low <= high:
#         mid = (low + high) // 2
#         attempt = list[mid]
#         if attempt == value:
#             return mid
#         elif attempt > value:
#             high = mid - 1
#         else:
#             low = mid + 1

#     return None


# new_list = [1, 4, 6, 7, 12, 23, 56, 89, 123, 232, 491, 519, 594, 607, 1235]

# print(binary_search(new_list, 607))
# print(binary_search(new_list, 23))
# print(binary_search(new_list, 2))


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
