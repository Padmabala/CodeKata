
def sort(arr,low,high):
    if(low<high):
        pivot=partition(arr,low,high)
        sort(arr,low,pivot-1)
        sort(arr,pivot+1,high)
def partition(arr,low,high):
    pivot=arr[high]
    i=low-1
    for j in range(low,high):
        if(arr[j]<pivot):
            i=i+1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[high]=arr[high],arr[i+1]
    return i+1
def alternateArray(arr,n):
    sort(arr,0,n)
    lIndex = 0
    rIndex = len(arr) - 1
    while 1:
        print(arr[rIndex], end=' ')
        rIndex -= 1
        if (lIndex >= rIndex):
            break
        print(arr[lIndex], end=' ')
        lIndex += 1



try:
    n=int(input())
    arr=list(map(int,input().split()[:n]))
    alternateArray(arr,len(arr)-1)
except:
    print("Enter only number")

