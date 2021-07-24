#p93
print("배열 크기 , 더해지는 횟수 , 연속할 수 입력해주세요")
n,m,k = map(int , input().split())
print("배열을 입력하세요")
data =list(map(int,input().split()))

data.sort()
first=data[n-1]
second=data[n-2]

result=0

while True:
  for i in range(k):
    if m==0: break
    result+=first
    m-=1
  if m ==0: break
  result+=second
  m-=1

print(result)

#2번째 방법
print("배열 크기 , 더해지는 횟수 , 연속할 수 입력해주세요")
n,m,k = map(int , input().split())
print("배열을 입력하세요")
data =list(map(int,input().split()))
#큰 수가 더해지는 횟수
count=int(m/(k+1))*k+m%(k+1)

result=0
result+=count*first + second * (m-count)

print(result)
