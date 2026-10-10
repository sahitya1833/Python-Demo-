import datetime
dob = datetime.date(2004,3,18)
today =  datetime.date.today()

age = today.year - dob.year

day_name = dob.strftime("%A , %B , %Y")

print("your age is:", age)
print("you were born on:", day_name)

