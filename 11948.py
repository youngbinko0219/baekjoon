a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())
# e와 f중 더 큰 값을 ef에 저장
ef = e if e>f else f
list=[a,b,c,d]
# 리스트를 내림차순으로 정렬
list = sorted(list,reverse=True)
print(list[0]+list[1]+list[2]+ef)