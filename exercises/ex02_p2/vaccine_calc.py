"""Vaccine calculator exercise as a structured program."""

from datetime import datetime, timedelta

__author__ = "730389248"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    population: int = int(input("Population: "))
    doses: int = int(input("Doses administered: "))
    doses_per_day: int = int(input("Doses per day: "))
    target: int = int(input("Target percent vaccinated: "))
    # TODO 2: Call days_to_target and store result in a variable.
    print(days_to_target(population, doses, doses_per_day, target))
    # TODO 4: Call future_date and store result in a variable.
    print(future_date(days_to_target))
    # TODO 5: Print the expected output using the variables above.

# TODO 1: Define days_to_target function
def days_to_target(population: int, doses: int, doses_per_day: int, target: int) -> int:
    population *= 2 
    num_vaxs: float = target / 100 
    days: int = round(((population) * (num_vaxs) - (doses)) / (doses_per_day))
    return days

# TODO 3: Define future_date function
def future_date(num_days: int) -> str:
    today: datetime = datetime.today()
    vax_day: timedelta = timedelta(num_days)
    vax: datetime = today + vax_day
    return "We will reach " + str(target)+ "% vaccination in " + str(vax_day.days)+ " days, which is "+ vax.strftime("%B %d, %Y")
if __name__ == "__main__":
    main()
