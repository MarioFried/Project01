#
# Example for working with Calendars
#

import calendar

c = calendar.HTMLCalendar(calendar.SUNDAY)
st = c.formatmonth(2018,2)
print(st)

c = calendar.TextCalendar(calendar.SUNDAY)
st = c.formatmonth(2018,2,0,0)
print(st)

for i in c.itermonthdays(2018,2):
    print (i)

for name in calendar.month_name:
    print (name)

for month_name in calendar.day_name:
    print (month_name)

print ("------------")
print ("Team Meetings will be on: ")
for m in range(1,13):
    cal = calendar.monthcalendar(2019,m)
    weekone = cal[0]
    weektwo = cal[1]
    if weekone[calendar.FRIDAY] != 0:
        meetday = weekone[calendar.FRIDAY]
    else:
        meetday = weektwo[calendar.FRIDAY]

    print ("%10s %2d" % (calendar.month_name[m],meetday))
