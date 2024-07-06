# 결과를 저장할 변수 result를 초기화
result = 0
# 4번 반복하여 사용자로부터 정수 입력받고 결과에 더하기
for i in range(4):
    # 사용자로부터 정수를 입력받아 result에 더하기
	result += int(input())
# 결과를 60으로 나는 몫 출력
print(result//60)
# 결과를 60으로 나눈 나머지 출력
print(result%60)