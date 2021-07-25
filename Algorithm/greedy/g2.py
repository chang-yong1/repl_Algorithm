#각 행의 최솟값이 가장 큰 값을 찾는 게임
#행렬 만들기
n , m =map(int , input().split())
data=[[0 for _ in range(m)] for _ in range(n)]
for row in range(n):
  a=input()
  data[row]=a.split()

find_min =0
for row in range(n):
  if int(min(data[row])) > int(find_min):
    find_min = min(data[row])
  
print("최댓값: ",find_min)

#sol 2
n,m=map(int , input().split())

result=0

for row in range(n):
  data=list(map(int , input().split()))
  find_min=min(data)
  result=max(result,find_min)

print(result)