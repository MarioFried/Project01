#
# Example for using TimeDelta Objects
#

from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta

print (timedelta(days=365,hours=5,minutes=1))
now = datetime.now()
print ("Today is ...................: " + str(now))
print ("One year from now it will be: " + str(now + timedelta(days=365)))
t = datetime.now() - timedelta(weeks=1)
print("One Week ago it was: ",t.strftime("%A %B %d, %Y"))

# Meu Aniversario
today = date.today()
mb = date(today.year,2,28)
# mb = date(today.year,12,25)
if mb < today:
    print("O Aniversario de Mario foi a %d dias atras" % (today-mb).days)
    mb = mb.replace(year=today.year+1)
    print("O Proximo Aniversario de Mario sera daqui a %d dias" % (mb-today).days)