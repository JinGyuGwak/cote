def solution(s, skip, index):
    answer = ''
    skip = set(ord(w) for w in skip)
    print(skip)
    for word in s:
        c = index
        word = ord(word)
        while c != 0:
            word += 1
            if word > ord('z'):
                word = word - ord('z') + ord('a') - 1
            if word in skip:
                continue
            c -= 1
        answer += chr(word)
    return answer

print(solution("aukks","wbqd",5))