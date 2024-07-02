# import는 시스셈 관련 기능을 제어하기 위한 모듈인 sys를 불려오는 것
import sys
T = int(input())
for i in range(T):
    # sys.stdin.readline()은 sys 모듈에 있는 stdin 객체의 메소드로 한 줄을 읽어오는 함수
    a,b = map(int, sys.stdin.readline().split())
    print(a+b)