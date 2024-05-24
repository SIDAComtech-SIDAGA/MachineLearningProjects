import datetime

# d = datetime.date(2016,7,24)
# print(d)

tday = datetime.date.today()
# print(tday.day)


#Ways of calling dates standards 
print(tday.weekday())
print(tday.isoweekday())

# tinedeltads 


tdelta = datetime.timedelta(days=7)
print(tday + tdelta)

print(tday - tdelta)

#date2 = datw1 + timedelta
##timedelta = date1 + date2

bday = datetime.date(2024,7,3)
tiil_bday = bday - tday
print(tiil_bday)
print(tiil_bday.days)
print(tiil_bday.total_seconds())





