total = 0

for i in range(5):
    tmp = int(input())
    # 만약 입력받은 값이 40보다 작으면
    if tmp < 40:
        # tmp 값을 40으로 설정함
        tmp = 40

    total += tmp

print(total // 5)