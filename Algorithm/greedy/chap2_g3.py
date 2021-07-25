#1110011 -> 연속된 1과 0 그룹을 세서 갯수가 적은 그룹을 뒤집자
#내코드
data=list(map(int,list(input())))
count_zero=0
count_one=0
# 101010 같은 상황일 때 구현 못함
for i in range(len(data)-1):
  if data[i] ==0 and data[i+1]!=data[i]:
    count_zero+=1
  elif data[i]==1 and data[i+1]!=data[i]:
    count_one+=1

if count_zero>=count_one:
  print(count_one)
else:
  print(count_zero)
  
#다른코드
data=input()
count0=0
count1=0

if data[0]=='0':
  count1+=1
else :
  count0+=1

for i in range(len(data)-1):
  if data[i]!=data[i+1]:
    if data[i+1]=='1':
      count0+=1
    else:
      count1+=1
print(min(count0,count1))