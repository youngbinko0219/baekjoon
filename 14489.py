a,b = map(int,input().split())
c = int(input())

if c*2<=a+b:
    print(a+b-c*2)
elif c*2>a+b:
    print(a+b)