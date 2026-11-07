# #First homework exercise

# from datetime import datetime, timedelta


# def get_days_from_today(date):
#     formats_to_try = ["%Y-%m-%d", "%d.%m.%Y", '%d/%m/%Y']
#     parsed_date = None   
#     for fmt in formats_to_try:
#         try:
#             parsed_date = datetime.strptime(date, fmt).date() #Конвертуємо рядок у дату,та використовуємо назву іншої змінної щоб не плутати з вхідним рядком
#             break
#         except (ValueError, TypeError):
#            continue

#     if parsed_date is None:
#         return "Помилка: Невірний формат дати. Будь ласка, використовуйте формат YYYY-MM-DD, DD.MM.YYYY або DD/MM/YYYY."
    
#     today = datetime.now().date() # Беремо поточну дату (без часу, щоб різниця була цілочисельною)
#     difference_days = (today - parsed_date).days # Знаходимо різницю в днях
#     return difference_days

# print(get_days_from_today("14.06.2023"))  # Приклад використання функції
# print(get_days_from_today("132321321"))  # Поверне текст помилки, якщо вказати будь що інше, крім формату дати
# print(get_days_from_today("13.14.2000")) # Поверне помилку бо 14 місяць не існує



# Second homework exercise

from random import random, randint

def get_numbers_ticket(min, max, quantity):
    if min < 1 or max > 1000 or min > max or quantity <= 0:
        return []

    total_numbers = (max - min ) + 1
    if quantity > total_numbers:
        return []
    
    numbers = set([])
     #Create an empty list to generate the sort numbers
    while len(numbers) < quantity:
        numbers.add(randint(min, max )) #Generate random numbers and add them to the list

    return sorted(numbers) #Sort the list and return it

incorrect_loterry_numbers = get_numbers_ticket(10, 14, 6) #При некорректих вхідних даних,функція повертає порожній список
print(f"Ваші лотерейні числа: {incorrect_loterry_numbers}")

loterry_numbers = get_numbers_ticket(1, 49, 6)
print(f"Ваші лотерейні числа: {loterry_numbers}")




