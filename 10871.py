n,x = map(int,input().split())
a = list(map(int,input().split()))
for i in range(n):
    if a[i]<x:
        print(a[i], end=" ")

# a = list(map(int,input().split()))
# x = int(input())
# for number in a:
#   if number<x:
#       print(number, end=" ")