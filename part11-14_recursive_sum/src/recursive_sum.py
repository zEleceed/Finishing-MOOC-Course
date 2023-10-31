# Please write a recursive function named recursive_sum(number: int) which calculates the sum 1 + 2 + ... + number.
# The exercise template contains the following outline:
def recursive_sum(number: int):
    # if the number is 1, there is nothing else to add
    if number <= 1:
        return number
    else:
        return number + recursive_sum(number - 1)

result = recursive_sum(3)
print(result)

print(recursive_sum(5))
print(recursive_sum(11))