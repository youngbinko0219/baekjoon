a,b,c = map(int,input().split())
if a==b==c:
    abc =  10000+(a*1000)
    print(abc)
elif a==b:
    ab = 1000+(a*100)
    print(ab)
elif a==c:
    ac = 1000+(a*100)
    print(ac)
elif b==c:
    bc = 1000+(b*100)
    print(bc)
else:
    print(100*max(a,b,c))