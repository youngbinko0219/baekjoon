a,b,c,d,e = input().split()
a = int(a)
b = int(b)
c = int(c)
d = int(d)
e = int(e)
f = ((a**2)+(b**2)+(c**2)+(d**2)+(e**2))%10
# a^2+b^2+c^2+d^2+e^2를 10으로 나누고 남은 나머지 를 변수 f에 저장
print(f)