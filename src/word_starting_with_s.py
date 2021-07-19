def word_starting_with_s(words):
    result_words = []
    for i in words:
        if i[0] == 's':
            result_words.append(i)
    return result_words


print(word_starting_with_s(["singer", "song", "amen", "flowers"]))
