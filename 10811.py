N,M=map(int, input().split())
Box=[]

for i in range(N):
    Box.append(i+1)

# print(Box)

for i in range(M):
    a,b=map(int, input().split())
    Temp=[]

    for j in range(b,a-1,-1):
       Temp.append(Box[j-1])

    for k in range(len(Temp)):
        Box[a+k-1] = Temp[k]

for i in range(N):
    print("{}".format(Box[i]), end=' ')