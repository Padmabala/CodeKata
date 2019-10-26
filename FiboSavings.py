def calculateTotalSavings(month,pastSavings):
    if(month in pastSavings):
        return pastSavings[month]
    else:
        total=calculateTotalSavings(month-1,pastSavings)+calculateTotalSavings(month-2,pastSavings)
        pastSavings[month]=total
    return total
noOfMonths=int(input())
pastSavings={}
pastSavings[0]=1000
pastSavings[1]=1000
calculateTotalSavings(noOfMonths,pastSavings)
sum=0
for i in range(noOfMonths+1):
    sum=sum+pastSavings[i]
print(sum)

