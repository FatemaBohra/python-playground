def reverse_string(s):
    a = ""
    for i in s:
        a = i + a
    return a


name = "Fatema Bohra"
print(reverse_string(name))
