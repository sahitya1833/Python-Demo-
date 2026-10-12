number = int(input("enter a number"))
num = number
ln = len(str(num))
total = 0
while num > 0:
    r = num % 10
    total = total + r ** ln
    num = num // 10

if total == number:
    print("number is armstrong..",total)
else:
    print("number is not armstrong" , total)
