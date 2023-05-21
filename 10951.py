import sys
lines = sys.stdin.readlines()

for line in lines:
    a,b=map(int, line.split())
    sum=a+b
    print(sum)

# for j in aa:
#     print(j)
