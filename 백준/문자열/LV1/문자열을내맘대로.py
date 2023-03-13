def solution(strings, n):
    c = 0
    for i in strings:
        strings[c] = i[n] + strings[c]
        c += 1

    strings.sort()
    c = 0
    for j in strings:
        strings[c] = j[1:]
        c += 1
    return strings