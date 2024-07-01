num = int(input())
# 변수 num을 선언하고 사용자로부터 정수값을 입력
sum = 0
# 변수 sum을 선언하고 초기화
for i in range(1,num+1):
# 1부터 사용자로부터 입력된 정수값을 반복
    sum+=i
    # 반복된 값을 합
print(sum)