number= int(input("enter a number"))
num = number
reverse = 0
while num > 0:
    r = num%10
    reverse= reverse*10
    num = num//10

if reverse == num:
    print("number is plaindrome..")
else :
    print ("number is not plaindrome..")