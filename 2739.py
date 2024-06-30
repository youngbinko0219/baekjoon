a = int(input())
# 변수 a를 선언하고 사용자로부터 입력을 받아 정수로 변환
if a<10 and a>=2:
# a가 2이상 10 미만인지 확인
    for i in range(1,10):
# 1부터 9까지 반복
        print(a ,"*",i,"=",a*i)
# a와 i를 곱한 값을 도스창에 출력