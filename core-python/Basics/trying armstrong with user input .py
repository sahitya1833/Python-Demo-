number = int(input("enter a number"))
num = number
ln = len(str(num))
sum = 0
while num > 0:
    r = num % 10
    sum = sum + r ** ln
    num = num // 10

if sum == number:
    print("number is armstrong..",sum)
else:
    print("number is not armstrong" , sum)
