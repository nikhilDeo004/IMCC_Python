import datetime

def get_nextDate():
    today=datetime.date.today()
    for i in range(7):
        yield today+datetime.timedelta(days=i)

for x in get_nextDate():
    print (x)