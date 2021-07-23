def thesaurus(*names):
    result = {}
    for i in sorted(names):
        char = i[0]
        if char in result:
            result[char] += [i]
        else:
            result[char] = [i]

    return result

print(thesaurus("Иван", "Мария", "Петр", "Илья"))