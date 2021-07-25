#1 , 0 더하기
#내 코드
str=input()
data=list(map(int,list(str)))
for i in range(len(data)-1):
  if data[i]<=1 or data[i+1]<=1:
    data[i+1]=data[i]+data[i+1]
  else:
    data[i+1]=data[i]*data[i+1]
print(data[-1])

#다른 코드
data=input()
result=int(data[0])

for i in range(i,len(data)):
  num=int(data[i])
  if num<=1 or result<=1:
    result+=num
  else:
    result*=num
print(result)