#Імпортуйте модуль datetime.
from datetime import datetime


#Створіть функцію get_days_from_today(date), яка розраховує кількість днів між заданою датою і поточною датою.
def get_days_from_today(date):
#Перетворіть рядок дати у форматі 'РРРР-ММ-ДД' у об'єкт datetime.
    datetime_object = datetime.strptime(date,"%Y-%m-%d")
#Отримайте поточну дату, використовуючи datetime.today().
    current_datetime = datetime.today()
#Розрахуйте різницю між поточною датою та заданою датою.
    difference_in_time = current_datetime.toordinal() - datetime_object.toordinal()
#Поверніть різницю у днях як ціле число.
    return difference_in_time
print(get_days_from_today("2024-12-05"))

#Вимоги до завдання:

#Функція приймає один параметр: date — рядок, що представляє дату у форматі 'РРРР-ММ-ДД' (наприклад, '2020-10-09').
#Функція повертає ціле число, яке вказує на кількість днів від заданої дати до поточної. Якщо задана дата пізніша за поточну, результат має бути від'ємним.

