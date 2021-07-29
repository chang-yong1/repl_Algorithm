n=int(input())
t = list(map(int,input().split()))
t.sort()
sum=0
for i in range(n):
  sum+=t[i]*(n-i)
print(sum)