
"""A vaccination calculator."""

__author__ = "730389248"

# The datetime data type is imported from the datetime library.
# A datetime object models a specific date and time.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime-objects
from datetime import datetime

# The timedelta data type is imported from the timedelta library.
# A timedelta object models a "time span", such as 1 day or 1 hour and 3 minutes.
# Subtracting two datetime objects will result in the timedelta between them.
# Adding a datetime and a timedelta will result in the datetime offset by the timedelta.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime.timedelta
from datetime import timedelta


# Begin your solution here...

population: int = int (input("Population: "))
doses_admin: int = int (input("Doses administered: "))
doses_day: int = int (input("Doses per day: "))
target_vacc: int = int (input("Target percent vaccinated: "))
num_vaxs: int = round (population * (doses_admin / 100))
num_days: int = round (num_vaxs / doses_day)
today : datetime = datetime.today()
vax_days: timedelta = timedelta(num_days)
vax_date: datetime = today + vax_days 
print("We will reach " + str(target_vacc) + "% vaccination in " + str(vax_days.days) + " days, which falls on " + vax_date.strftime("%B %d, %Y"))
 