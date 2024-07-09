li = list(map(int,input().split()))
x,y,r = map(int,input().split())
# x가 li 리스트에 존재하면 그 인덱스에 1을 더한 값을 출력하고, 그렇지 않으면 0을 출력
print(li.index(x)+1 if x in li else 0)