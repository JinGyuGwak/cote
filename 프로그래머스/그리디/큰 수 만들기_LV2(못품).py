# string 형변환 하는법 (인트형으로, 리스트 형으로) 공부
def solution(number, k):
    stack = []
    for num in number:
        # 문자열 맨 앞에는 가장 큰 숫자가 오는게 좋음
        while stack and stack[-1] < num and k > 0:
            k -= 1
            stack.pop()
        stack.append(num)
    if k != 0:
        stack = stack[:-k]
    return ''.join(stack)
print(solution("1924", 2))



'''
join 함수 -> 리스트 배열을 문자열로 합치기

a=["12/c","3","e"]
string = ''.join(a)
print(string)  -> 12/c3e

문자열 사이에 특정 글자 넣기
string ='/'.join(a) -> 1/2/c/3/e

리스트 배열이 정수형일 땐 리스트 정수형을 리스트 문자열로 변환 후 바꿔야함
a=[0,1,2,3]
print(''.join(str(i) for i in a)


'''