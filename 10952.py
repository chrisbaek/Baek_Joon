# chance=int(input())

# for i in range(chance):
#     a,b=map(int, input().split())
#     sum=a*b
#     aa.append(sum)
# for j in aa:
#     print(j)

aa=[]
a=None
b=None

while True :
    a,b=map(int, input().split())
    if a==0 and b==0:
        break
    sum=a+b
    aa.append(sum)

for j in aa:
    print(j)