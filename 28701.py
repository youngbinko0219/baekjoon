N = int(input())
sum = 0
sumCube = 0
for i in range(1,N+1):
    # 1부터 N까지 반복하면서 합산
    sum+=i
    # 1부터 N까지 반복하면서 세제곱을 계산하여 합산
    sumCube+=i**3
print(sum)
print((sum)**2)
print(sumCube)