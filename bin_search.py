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


# new_list = ["as", "fgd", "gti", "h", "itwe", "klw"]

# print(binary_search(new_list, "fgd"))


def binary_search(arr, val):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = low + (high - low) // 2
        mid_val = arr[mid]

        if mid_val == val:
            return mid
        elif mid_val > val:
            high = mid - 1
        else:
            low = mid + 1

    return None


new_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(binary_search(new_arr, 1))
