#공포도 별 모험가 그룹 나누기
#내 코드
n=int(input("모헙가의 수 입력하세요"))
data=list(map(int,input().split()))
data.sort()
#5명 공포도 3이하의 공포도를 가진 사람들(3명)으로 구성
count=0
max_scared=max(data)
while(True):
  if ( len(data) >= max_scared ):
    for _ in range(max_scared):
      del data[n-1]
      n-=1
    count+=1
    if len(data)==0:
      break
    max_scared=max(data)
  elif len(data) < max_scared:
    data.remove(max_scared)
    n-=1
    max_scared = max(data)
    if len(data)==0:
      break
  
  
 #3 3 3 3 1 -> 1 3 
print(count)
# 새로운 코드
n=int(input("모헙가의 수 입력하세요"))
data=list(map(int,input().split()))
data.sort()
#총 그룹 수
result=0
#그룹 포함된 모험가 수
count=0

for i in data:
  count+=1
  if count >= i:
    result+=1
    count=0
  #여긴 내가 추가한 부분

print(result)