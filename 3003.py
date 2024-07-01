stdChess = [1,1,2,2,2,8]
outputChess = []
inputChess = list(map(int,input().split()))
for i in range(6):
    num = stdChess[i]-inputChess[i]
    outputChess.append(num)
    print(outputChess[i],end=" ")