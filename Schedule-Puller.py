import pandas as pd
from gcsa.event import Event
from gcsa.google_calendar import GoogleCalendar
from gcsa.recurrence import Recurrence, DAILY, SU, SA
from datetime import date, datetime


# column 2-9
# assign days to column #  2 Sunday, 8 Saturday
# line 11 Date, consistent

target = r'/home/based/Projects/Schedule Puller/schedule/Welcome.html'
tables = pd.read_html(target) # Returns list of all tables on page

# for i in range(2,9): # table 15, column # (2-9), line (11)
#     # print(tables[15][i][7])
#     # print(tables[15][i][11])
#     events = tables[15][i][11]

# def shiftdate(month, day):
#     d = date(year=2022, month, day)

shifts_dates = [tables[15][i][7] for i in range(2,9)]
shifts = [tables[15][i][11] for i in range(2,9)]

print(shifts)
print(shifts_dates)
seperated = str(shifts_dates)
# print(seperated.split('/'))

# grouped = [item for sublist in zip(shifts_dates, shifts) for item in sublist]
# print(grouped)

zipped = [list(i) for i in zip(shifts_dates, shifts)]

print(zipped[1][1])

zippedplus = [zipped[i] for i in range(0,7)]

print(zippedplus)

if 'nan' in str(zipped[1][1]):
    print("success")

from beautiful_date import Apr, hours
from gcsa.event import Event

def create_event(date, time, time_2):
    start = (date)[time]
    end = (date)[time_2]
    event = Event('Meeting',
                start=start,
                end=end)
# date = 
# month =
# shiftdate(month, day)


# calendar = GoogleCalendar('iamhirojl@gmail.com')

# convert month # to month in name, keep day value same and replace, 2022 default

def make_schedule():
    event = Event(
        'Wegmans',
        start=(1 / Jan / 2022)[9:00],
        recurrence=[
            Recurrence.rule(freq=DAILY),
            Recurrence.exclude_rule(by_week_day=[SU, SA]),
            Recurrence.exclude_times([
                (19 / Apr / 2022)[9:00],
                (22 / Apr / 2022)[9:00]
            ])
        ],
        minutes_before_email_reminder=50
    )
    # calendar.add_event(event) # add so this runs after 



# for event in calendar:
    # print(event)
