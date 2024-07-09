A, B, C, D = map(int, input().split())  # 입력된 값을 공백 기준으로 나누어 정수형으로 변환합니다.
result = (A + D) - (B + C)  # (A+D)와 (B+C)의 차이를 계산합니다.
if result < 0:  # 결과가 음수인 경우
    result = -result  # 부호를 반전시켜 양수로 만듭니다.
print(result)  # 결과를 출력합니다.