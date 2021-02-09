from datetime import timedelta
from datetime import datetime

population: int = int(input("Population: "))
doses_admin: int = int(input("Doses administered: "))
doses_day: int = int(input("Doses per day: "))
target_vacc: int = int(input("Target percent vaccinated: "))
num_vaxs: float = target_vacc / 100
if doses_admin >= doses_day: 
    num_days: int = round(((num_vaxs) * (population)) / (doses_day))
elif doses_admin < doses_day:
    num_days: int = round(((num_vaxs) * (population)) / (doses_day) * ((doses_admin) / (doses_day))
today: datetime = datetime.today()
vax_days: timedelta = timedelta(num_days)
vax_date: datetime = today + vax_days 
vax_date = vax_date.strftime("%B %d, %Y")
print("We will reach " + str(target_vacc) + "% vaccination in " + str(vax_days.days) + " days, which falls on " + vax_date)


#if doses_admin >= doses_day: 
    #num_days: int = round(((num_vaxs) * (population)) / (doses_day))
#else:
    #num_days: int = round(((num_vaxs) * (population)) / (doses_day) * ((doses_admin) / (doses_day))

    #vax = vax.strftime("%B %d, %Y") 

#vax: datetime = vax.strftime("%B %d, %Y") 