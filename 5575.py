# 첫 번째 시간 범위 입력 받기 (시, 분, 초)
a, b, c, a1, b1, c1 = map(int, input().split())
# 두 번째 시간 범위 입력 받기 (시, 분, 초)
d, e, f, d1, e1, f1 = map(int, input().split())
# 세 번째 시간 범위 입력 받기 (시, 분, 초)
g, h, i, g1, h1, i1 = map(int, input().split())

# 시간 차이 계산 및 출력
# 첫 번째 줄
# 끝 시간과 시작 시간의 차를 초로 계산하고 시간, 분, 초로 변환하여 출력
# 끝 시간과 시작 시간의 차를 초 단위로 계산
diff1 = (a1 - a) * 3600 + (b1 - b) * 60 + (c1 - c)
# 초를 시간으로 변환
hours1 = diff1 // 3600
# 남은 초를 분으로 변환
minutes1 = (diff1 % 3600) // 60
# 남은 초
seconds1 = diff1 % 60
print(hours1, minutes1, seconds1)

# 두 번째 줄
# 끝 시간과 시작 시간의 차를 초로 계산하고 시간, 분, 초로 변환하여 출력\
# 끝 시간과 시작 시간의 차를 초 단위로 계산
diff2 = (d1 - d) * 3600 + (e1 - e) * 60 + (f1 - f)
# 초를 시간으로 변환
hours2 = diff2 // 3600
# 남은 초를 분으로 변환
minutes2 = (diff2 % 3600) // 60
# 남은 초
seconds2 = diff2 % 60
print(hours2, minutes2, seconds2)

# 세 번째 줄
# 끝 시간과 시작 시간의 차를 초로 계산하고 시간, 분, 초로 변환하여 출력
# 끝 시간과 시작 시간의 차를 초 단위로 계산
diff3 = (g1 - g) * 3600 + (h1 - h) * 60 + (i1 - i)
# 초를 시간으로 변환
hours3 = diff3 // 3600
# 남은 초를 분으로 변환
minutes3 = (diff3 % 3600) // 60
# 남은 초
seconds3 = diff3 % 60
print(hours3, minutes3, seconds3)