import datetime

t = datetime.time
time = datetime.time(9,30,45,10000)
print(time.hour)
print(time.min)
print(time.second)
print(time.microsecond)

time2 = datetime.datetime(2016,7,4,12,30,45,1000)
print(time2)
print(time2.time())

tdelta  = datetime.timedelta(days=7)
print(time2 + tdelta)


Sidaga = datetime.datetime.today()
Sidaga2 = datetime.datetime.now()

Sidaga3 = datetime.datetime.utcnow()
print(Sidaga)
print(Sidaga2)
print(Sidaga3)

