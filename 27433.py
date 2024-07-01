a = int(input())
fact = 1
# 팩토리얼 변수 초기화
for i in range(1,a+1):
    fact*=i
    # 1부터 a까지의 모든 수를 곱함
print(fact)