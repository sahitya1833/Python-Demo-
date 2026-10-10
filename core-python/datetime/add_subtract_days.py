import datetime
today = datetime.date.today()
future = today + datetime.timedelta(days=10)
past = today - datetime.timedelta(days=7)

print("today:", today)
print("days later:", future)
print("7 days ago :", past)

