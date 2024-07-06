# 사용자로부터 정수 n을 입력받음
n = int(input())

# 1부터 n까지 반복
for i in range(1,n+1):
    # 각 반복마다 문자열을 입력받음
    data = input()
    # 입력받은 문자열을 앞에 인덱스를 붙여 출력
    print("%d. %s"%(i,data))