N=int(input())

score=list(map(int, input().split()))

if N!=len(score):
   print("다시 입력해주세요")
   score=list(map(int, input().split()))

new_score=[]
for i in range(N):
    new_score.append(0)

for i in range(N):
    new_score[i]=score[i]/max(score)*100

sum = 0

for i in range(N):
    sum = sum + new_score[i]

average=sum/N

print(round(average,5))



