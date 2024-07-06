# 버거 가격을 저장할 빈 리스트 생성
burger = []
# 음료 가격을 저장할 빈 리스트 생성
drink = []
# 버거 가격 입력받기
for i in range(3):
    # 사용자로부터 정수 입력받음
    a = int(input())
    # 입력받은 가격을 버거 리스트에 추가
    burger.append(a)
    
# 음료 가격 입력받기
for i in range(2):
    # 사용자로부터 정수 입력받음
    b = int(input())
    # 입력받은 가격을 음료 리스트에 추가
    drink.append(b)
    
# 최소 버거 가격과 최소 음료 가격을 합하여 50을 뺀 값을 출력
print(min(burger)+min(drink)-50)