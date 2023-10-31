# Please write a recursive function named add_numbers_to_list(numbers: list). The function takes a list of numbers as
# its argument, and adds new numbers to the list until the length of the list is divisible by five. Each number added
# to the list should be one greater than the last number in the list.
#
# The function must call itself recursively. Please see the example below.
#
# numbers = [1,3,4,5,10,11]
# add_numbers_to_list(numbers)
# print(numbers)


def add_numbers_to_list(numbers: list):
    x = len(numbers)
    if x % 5 == 0:
        return numbers
    else:
        maxnumber = max(numbers)
        maxnumber += 1
        numbers.append(maxnumber)
        return add_numbers_to_list(numbers)


numbers = [1, 3, 4, 5, 10, 11]
add_numbers_to_list(numbers)
print(numbers)
