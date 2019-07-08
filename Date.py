#
# Exemplo de Programa em Python com usa Informacoes Date
#

from datetime import date
from datetime import time
from datetime import datetime

def main():
  today = date.today()
  days=["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
  print ("Today's date is:", today)
  print ("Date Components: ", today.day,"/", today.month,"/", today.year)
  print ("Today Weekday's # is: ",today.weekday())
  print ("Which is :",days[today.weekday()])

  now = datetime.now()
  print ("The current datetime is: ",now)
  t = datetime.time(datetime.now())
  print (t)
  print ("Hour: ..........",t.hour)
  print ("Minute: ........",t.minute)
  print ("Second : .......",t.second)
  print ("Milisecond : ...",t.microsecond)

if __name__ == "__main__":
    main()
