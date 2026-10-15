num=[1,2,3,5]
def missing_num(num,n):
    sum1=(n*(n+1))/2
    sum2=sum(num)
    return int(sum1-sum2)
print(missing_num(num,5))

