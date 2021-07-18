def odd_integers(numbers):
    result_odd = []
    for i in numbers:
        if i % 2 != 0:
            result_odd.append(i)
    return result_odd


print(odd_integers([2, 4, 3, 5, 7, 9, 99]))
