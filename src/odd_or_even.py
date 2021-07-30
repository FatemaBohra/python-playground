# Given a list of integers, determine whether the sum of
# its elements is odd or even.

def odd_or_even(arr):
    sum = 0
    for i in arr:
        sum += i
    return "even" if sum % 2 == 0 else "odd"


print(odd_or_even([1, 2, 5]))
