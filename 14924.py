# 기차의 속도 s 파리의 속도 t 처음 두 기차의 거리 d
s,t,d = map(int,input().split())
meet = d/(s*2)
f = meet*t
print(int(f))