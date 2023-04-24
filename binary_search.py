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


def binary_search_practice(arr, val):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if val == arr[mid]:
            return mid
        elif val < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1

    return None


new_arr = [1, 3, 5, 7, 8, 11, 14, 19]

print(binary_search_practice(new_arr, 1))
print(binary_search_practice(new_arr, 3))
print(binary_search_practice(new_arr, 4))
print(binary_search_practice(new_arr, 5))
print(binary_search_practice(new_arr, 7))
print(binary_search_practice(new_arr, 8))
print(binary_search_practice(new_arr, 11))
print(binary_search_practice(new_arr, 14))
print(binary_search_practice(new_arr, 19))
