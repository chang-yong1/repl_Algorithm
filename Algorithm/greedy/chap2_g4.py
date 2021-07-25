n=input("숫자입력: ")
data=list(map(int,input().split()))
data.sort(reverse=True)
if data[len(data)-1]>1:
  print(1)

find=2
while(True):
  count=find
  for i in range(len(data)):
    if count-data[i]>=0:
      count-=data[i]
    elif count==0:
      break
  if count!=0:
    break

  find+=1

print(find)

