n=int(input())
arr=list(map(int,input().split()[:n]))
sum=0
for i in range(len(arr)):
    sum=sum+arr[i]
if(sum%2==0 and sum%3==0 and sum%5==0):
    print("1")
else:
    print("0")