N,M=map(int, input().split(' '))
basket=[]

for n in range(N):
    basket.append(0)

for m in range(M):
    a,b,k=map(int, input().split(' '))
    for i in range(a-1,b):
        basket[i]=k

for n in range(N):
    print(str(basket[n])+" ", end='')
