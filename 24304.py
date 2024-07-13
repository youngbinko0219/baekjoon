x = int(input())
n = int(input())
tot = 0
for i in range(n):
    price,cnt = map(int,input().split())
    tot += (price*cnt)

if x == tot:
    print("Yes")
else:
    print("No")