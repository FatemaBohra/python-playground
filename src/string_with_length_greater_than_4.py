def string_with_length_greater_than_4(words):
    result = []
    for i in words:
        if len(i) > 4:
            result.append(i)
    return result


print(string_with_length_greater_than_4(["words", "string", "Fatema", "no"]))

