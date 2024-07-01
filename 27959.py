a,b = map(int,input().split())
# 만약 a*100이 b보다 크거나 같으면 yes 출력
# 그 외의 경우 no 출력
if a*100>=b:
    print("Yes")
else:
    print("No")