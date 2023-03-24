def solution(cards1, cards2, goal):
    answer = ''
    i1 = 0
    i2 = 0
    print(len(cards1))
    for i in goal:
        if i1 < len(cards1) and cards1[i1] == i:
            i1 += 1

        elif i2 < len(cards2) and cards2[i2] == i:
            i2 += 1

        else:
            return 'No'
    return 'Yes'

solution(["i", "water", "drink"],["want", "to"],["i", "want", "to", "drink", "water"])