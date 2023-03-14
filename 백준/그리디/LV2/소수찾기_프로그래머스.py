from itertools import permutations
def solution(numbers):
    answer = 0
    nums = []

    for i in range(1, len(numbers) + 1):
        nums.append(list(set(map(''.join, permutations(numbers, i)))))
    per = list(set(map(int, set(sum(nums, [])))))

    for p in per:
        if check(p):
            answer += 1
    return answer


def check(x):
    if x <= 1: return 0
    for i in range(2, x):
        if x % i == 0:
            return 0
    return 1



print(solution("17"))