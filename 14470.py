a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

# 만약 a가 음수라면
if a < 0:
    # -a*c+d+b*e를 계산하여 변수 time에 저장
    time = -a * c + d + b * e
else:
    time = (b - a) * e

print(time)