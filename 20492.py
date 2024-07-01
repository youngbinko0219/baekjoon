a = int(input())
firRes = a-(a*22/100)
# firRes = 첫번째 결과로 상금에서 22%가 빠진것
secRes = a-((a*20/100)*22/100)
# secRes =  두번째 결과로 상금의 20%에 대해 22%가 빠진것
print(int(firRes),int(secRes))