# exercise 1
def power(a, b):
    if a <= 0 or b <= 0:
        return - 1
    elif b == 1:
        return a
    else:
        return a * power(a, b-1)


print(power(3, 4))
print(power(-1, 3))


# exercise 2
def binary_search(numbers, num):

    # 1. The base case has to be set -> if the element is not in the list, then it return -1
    if not numbers:
        return -1

    # 2. The midpoint of the list has to be calculated
    mid = len(numbers) // 2

    # 3. If the middle element matches the element we are searching for, then the function should return its midpoint
    if numbers[mid] == num:
        return mid

    # 4. If 3. was not the case then the function needs to continue searching
    # If the middle element is greater than the element we are searching for: left half of the list needs to be searched
    elif numbers[mid] > num:
        left_half = numbers[:mid]
        return binary_search(left_half, num)

    # 5.If the middle element is less than the element we are searching for: right half of the list needs to be searched
    else:
        right_half = numbers[mid+1:]
        index = binary_search(right_half, num)
        return -1 if index == -1 else mid + 1 + index


numbers = [1, 2, 6, 8, 10, 12, 16, 18]
search_num = 12
binary_search(numbers, search_num)
print(binary_search(numbers, search_num))
search_num = 7
binary_search(numbers, search_num)
print(binary_search(numbers, search_num))