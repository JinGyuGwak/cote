from collections import Counter


def solution(k, tangerine):
    answer = 0
    counter = Counter(tangerine)
    # {3: 2, 2: 2, 5: 2, 1: 1, 4: 1}
    print(counter.items())
    a = sorted(counter.items(), key=lambda x: x[1], reverse=True)
    print(a)

    # 정렬된 딕셔너리로 귤 개수 맞추기
    cnt = 0
    for i in a:
        k -= i[1]
        answer += 1

        if k <= 0:
            break

    return answer
print(solution(6,[1, 3, 2, 5, 4, 5, 2, 3]))