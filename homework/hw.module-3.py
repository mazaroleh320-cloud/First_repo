#First homework exercise

from datetime import datetime, timedelta


def get_days_from_today(date):
    date = datetime.strptime(date, "%Y-%m-%d").date() #Convert the string to a date object

    today = datetime.now().date()
    difference_days = (today - date).days # Find the difference between two dates
    return difference_days

print(get_days_from_today("2026-03-09"))




# Second homework exercise

from random import random, randint

def get_numbers_ticket(min, max, quantity):
    numbers = set([]) #Create an empty list to generate the sort numbers
    while len(numbers) < quantity:
        numbers.add(randint(min, max + 1)) #Generate random numbers and add them to the list
    return sorted(numbers) #Sort the list and return it

loterry_numbers = get_numbers_ticket(1, 49, 6)
print(f"Ваші лотерейні числа: {loterry_numbers}")




