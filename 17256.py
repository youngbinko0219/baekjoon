ax,ay,az = map(int,input().split())
cx,cy,cz = map(int,input().split())
print(cx-az,cy//ay,cz-ax)
# a@b = az+bx, ay*by, ax+bz = cx,cy,cz
# a@b=c를 만족하는 @수 b를 계산
# bx=cx-az, by=cy/ay bz = cz-ax