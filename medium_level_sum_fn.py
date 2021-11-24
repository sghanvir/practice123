sum2 = 0
a = list(map(int,input('Enter multiple values').split()))
print('Entered list :',a)
for i in range(0,len(a)):
    sum2 = sum2 + a[i]
print('sum of entered numbers is {}'.format(sum2))