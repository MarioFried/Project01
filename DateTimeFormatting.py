#
# Formatting Date and Time Output
#

from datetime import datetime

def main():
    now = datetime.now()
    print (now)

# Date Formatting
# %y/%Y - Year, %a/%A - Weekday, %b/%B - Month, %d - day of month
    print (now.strftime("The current Year is: %Y"))
    print (now.strftime("%a, %d %b, %y"))
    print (now.strftime("%A, %d %B, %Y"))

# %c - locale's date and time, %x - locale's date, %X - locale's time
    print (now.strftime("Locale Date and Time: %c"))
    print (now.strftime("Locale Date ........: %x"))
    print (now.strftime("Locale Time ........: %X"))

# %I/%H - 12/24 Hour, %M - Minute, %S - Second, %p - locale's AM/PM
    print (now.strftime("Current Time: %I:%M:%S ,%p"))
    print (now.strftime("Current Time: %H:%M:%S"))


if __name__ == "__main__":
    main()