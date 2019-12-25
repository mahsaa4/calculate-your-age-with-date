from datetime import date
import sys


class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def Today(self):
        return date.today()

    def date(self):
        return list((self.year, self.month, self.day))


if __name__ == '__main__':
    date_entry = input()
    year, month, day = list(map(int, date_entry.split('/')))
    date1 = Date(year=year, month=month, day=day)
    my_date = []
    my_date.append(date1.date())
    today = date1.Today()
    born_year = my_date[0][0]
    born_month = my_date[0][1]
    born_day = my_date[0][2]
    age = today.year - born_year
    if today.month < born_month or today.month == born_month and today.day < born_day:
        age -= 1
    if born_month > 12:
        print("WRONG")
        sys.exit(0)
    if born_day > 31:
        print("WRONG")
        sys.exit(0)
    print(age)
