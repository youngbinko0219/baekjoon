n,m,k = map(int,input().split())
# 둘 중 작은것 + 둘 중 큰것
print(min(m,k)+n - max(m,k))