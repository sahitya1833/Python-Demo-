number = 153
num= number
sum = 0
while num > 0:
    r = num%10
    sum = sum + r*r*r
    num = num//10
if sum == number:
    print("number is armstrong..",sum)
else:
    print("number is not armstrong..", sum)
