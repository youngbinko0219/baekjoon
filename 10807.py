# 정수의 개수 n, 정수 n_list, 찾으려는 정수 v를 입력
n = int(input())
n_list = list(map(int,input().split()))
v = int(input())
# n_list 중 v가 몇 개인지 출력
cnt = 0
for i in n_list:
    if i == v:
        cnt += 1
print(cnt)