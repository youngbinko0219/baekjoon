N,A,B = map(int,input().split())
# N = 걷는시간 A = 버스기다리는 시간 B = 지하철까지 가는 시간
# 1<=a<=10^6
# 1<=c<=b<=10^6
# c는 b보다 작거나 같으니 신경 쓸 필요 없다.
if A<B:
    print("Bus")
elif A>B:
    print("Subway")
else:
    print("Anything")