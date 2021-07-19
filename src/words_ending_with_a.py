def words_ending_with_a(words):
    results = []
    for i in words:
        if i[-1] == 'a':
            results.append(i)
    return results


print(words_ending_with_a(["histeria", "collaboration", "laptop"]))