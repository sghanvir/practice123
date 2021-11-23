sum1 = 0
a = list(map(int,input('Enter values').split()))
print('Entered list :',a)
for i in range(0,len(a)):
    sum1 = sum1 + a[i]
print('sum of entered numbers is {}'.format(sum1))