while True:
    # 사용자로부터 공백을 기준으로 정수 두 개 입력받기
    a,b = map(int,input().split(" "))
    # 만약 입력받은 두 정수가 모두 0이면 반복문 종료
    if a==0 and b==0:
        break
    # 입력받은 두 정수를 더한 결과 출력
    print(a+b)