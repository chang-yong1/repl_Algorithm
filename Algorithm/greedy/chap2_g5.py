#볼링공 고르기
import time
n, max_m=map(int ,input().split())
ball=list(map( int , input().split()))
count=0
start_time=time.time()
for i in range(len(ball)):
  for j in range(i,len(ball)):
    if ball[i] != ball[j]:
      count+=1
end_time=time.time()
print(count)
print(end_time - start_time)

#다른 코드
n ,m= map(int , input().split())
data=list(map(int, input().split()))

array=[0]*11
for x in data:
  array[x]+=1
result=0

for i in range(1,m+1):
  n-=array[i]
  result+=array[i]*n

print(result)
