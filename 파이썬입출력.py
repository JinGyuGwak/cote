#input은 한 줄의 문자열을 입력 받도록 해줌, 그 후 int로 묶어서 정수로 변환
#list(map(int,input().split())) 가장 안쪽 괄호인 input.split()로 리스트 입력받음
#그 후 map을 이용하여 해당리스트의 모든 원소에 int() 적용
#그 결과를 list()로 바꿈

n= int(input())
a=list(map(int,input().split()))
print(f"하나입력값 = {n}\n리스트 입력값 = {a}")
a,b,c=map(int,input().split())
print("a는",a,"b는",b,"c는",c)

#코드가 길 경우 입력방식 ,
#readline()은 엔터를 줄바꿈 기호로 입력되어서 뒤에 rstrip을 써주므로 이를 방지
#rstrip(값)  문자열의 맨 오른쪽부터 검사하여 값 과 같으면 지움 위에 경우 공백
#lstrip(값) 도 있음
import sys
data=sys.stdin.readline().rstrip()

print(data)
