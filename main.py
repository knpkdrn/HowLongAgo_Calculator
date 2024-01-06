import datetime
from dateutil import relativedelta
from tkinter import *
from tkcalendar import Calendar

root = Tk()
root.title("HowLongAgo? Calculator")
root.geometry("1000x500")
root.minsize(1000, 500)
root.maxsize(1000, 500)

# add first calendar
today = datetime.date.today()
cal_from = Calendar(root, selectmode="day", year=today.year, month=today.month, day=today.day)
cal_from.pack(pady=20, padx=40)
cal_from.pack(side=LEFT)

# add second calendar
cal_to = Calendar(root, font="Arial 9", selectmode="day", year=today.year, month=today.month, day=today.day)
cal_to.pack(pady=20, padx=40)
cal_to.pack(side=RIGHT)


def parse_date(date_str):
    date_formats = ["%m/%d/%Y", "%m/%d/%y", "%m-%d-%Y", "%m-%d-%y"]

    for date_format in date_formats:
        try:
            return datetime.datetime.strptime(date_str, date_format).date()
        except ValueError:
            pass

    raise ValueError("Invalid date format")


def calc_diff():
    negative = False
    date_from_str = cal_from.get_date()
    date_to_str = cal_to.get_date()
    print(date_from_str)

    # Custom parsing to handle non-zero-padded day and month
    date_from = parse_date(date_from_str)
    date_to = parse_date(date_to_str)

    if date_to < date_from:
        date_from = parse_date(date_to_str)
        date_to = parse_date(date_from_str)
        negative = True
    elif date_to == date_from:
        date.config(text=f"{cal_to.get_date()} is today.")
        return

    all_days = abs((date_to - date_from).days)
    delta = relativedelta.relativedelta(date_to, date_from)
    if not negative:
        date.config(text=f"{date_to} is {all_days} days away.\n{date_to} was {delta.years} years, {delta.months} months, and {delta.days} days ago.")
    else:
        date.config(text=f"{date_to} was {all_days} days ago.\n{date_to} was {delta.years} years, {delta.months} months, and {delta.days} days ago.")


# Add Button and Label
date = Label(root, text="")
date.pack(pady=20, side=BOTTOM)

Button(root, text="Get Date", command=calc_diff).pack(pady=40, side=BOTTOM)

# execute Tkinter
root.mainloop()
