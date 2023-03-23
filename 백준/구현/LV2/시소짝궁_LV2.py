from itertools import permutations
from collections import Counter

weight_cnt = Counter([100,200,300])
arr = [2,3,4]
nPr = permutations(arr, 2)
print(list(nPr))
print(weight_cnt)
for i in weight_cnt: #key 값 순회
    print(i)
#출력 : [(A,B) (A,C) (B,A) (B,C) (C,A) (C,B)]