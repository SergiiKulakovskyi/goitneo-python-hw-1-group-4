from collections import defaultdict
from datetime import datetime

weekday_names = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
]


def get_birthdays_per_week(users):
    birthday_dict = defaultdict(list)
    today = datetime.today().date()
    current_weekday = today.weekday()

    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()
        birthday_this_year = birthday.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday.replace(year=today.year + 1)

        delta_days = (birthday_this_year - today).days
        birthday_weekday = birthday_this_year.weekday()
        if birthday_weekday in [5, 6]:
            delta_days += 7 - birthday_weekday

        if delta_days < 7:
            greeting_weekday = (current_weekday + delta_days) % 7
            birthday_dict[weekday_names[greeting_weekday]].append(name)

    for day, names in birthday_dict.items():
        print(f"{day}: {', '.join(names)}")


users = [
    {"name": "Elon Musk", "birthday": datetime(1971, 10, 23)},
    {"name": "Bill Gates", "birthday": datetime(1955, 10, 19)},
    {"name": "Linus Torvalds", "birthday": datetime(1969, 10, 20)},
    {"name": "Mark Zuckerberg", "birthday": datetime(1984, 10, 21)},
    {"name": "Tim Berners-Lee", "birthday": datetime(1955, 10, 22)},
    {"name": "Larry Page", "birthday": datetime(1973, 10, 24)},
    {"name": "Sergey Brin", "birthday": datetime(1973, 10, 25)},
    {"name": "Steve Wozniak", "birthday": datetime(1950, 8, 11)},
    {"name": "Markus Persson", "birthday": datetime(1979, 6, 1)},
    {"name": "Jeff Bezos", "birthday": datetime(1964, 1, 12)},
    {"name": "Steve Jobs", "birthday": datetime(1955, 2, 24)},
    {"name": "Ada Lovelace", "birthday": datetime(1815, 12, 10)},
    {"name": "Grace Hopper", "birthday": datetime(1906, 12, 9)},
    {"name": "Alan Turing", "birthday": datetime(1912, 6, 23)},
    {"name": "Tim Cook", "birthday": datetime(1960, 11, 1)},
    {"name": "Richard Stallman", "birthday": datetime(1953, 3, 16)},
    {"name": "Guido van Rossum", "birthday": datetime(1956, 1, 31)},
    {"name": "Bjarne Stroustrup", "birthday": datetime(1950, 12, 30)},
    {"name": "Vint Cerf", "birthday": datetime(1943, 6, 23)},
    {"name": "Rasmus Lerdorf", "birthday": datetime(1968, 11, 22)},
]

get_birthdays_per_week(users)
