#n = int(input())
#fac_sum = 0
#for i in range(1, n+1):
 #  fac *= i
#fac_sum += fac
#print(fac_sum)


n = int(input())

nums = []
for i in range(0, n, 1):
    row = []
    for j in range(0, n, 1):
        row.append(0)
    nums.append(row)

print(nums)


   
