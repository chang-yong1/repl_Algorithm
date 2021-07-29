n , k=map(int , input().split())
data=[]
count=0
for i in range(n):
  money =int(input())
  data.append(money)
    
for i in range(n):
  if k >= data[n-i-1]:
    count+=k//data[n-i-1]
    k=k%data[n-i-1]
print(count)