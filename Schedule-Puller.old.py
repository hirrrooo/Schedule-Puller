import pandas as pd
from gcsa.event import Event
from gcsa.google_calendar import GoogleCalendar
from gcsa.recurrence import Recurrence, DAILY, SU, SA
from datetime import date, datetime
from pathlib import Path

data_folder = Path('schedule')
# column 2-9
# assign days to column #  2 Sunday, 8 Saturday
# line 11 Date, consistent

target = data_folder / 'Welcome.html'
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


from gcsa.event import Event

def create_event(month, day, hour, minute, year = 2022):
    start = (datetime(month, day, hour, minute, year))
    end = (datetime(month, day, hour, minute, year))
    event = Event('Meeting',
                start=start,
                end=end)
# date = 
# month =
# shiftdate(month, day)
dp = 0
Sun = zippedplus[0][0]
SunShift = zippedplus[0][1]
SunShiftTimes = SunShift.split('-')

def ShiftStartTimes():
    print("Shift Start Times Output")
    zippedplus[x][0] for x in range(0,7):
        print(zippedplus[x][0])
ShiftStart = SunShiftTimes[0]
print(ShiftStart)
ShiftStartTimes()
# calendar = GoogleCalendar('iamhirojl@gmail.com')

# convert month # to month in name, keep day value same and replace, 2022 default

    # calendar.add_event(event) # add so this runs after 



# for event in calendar:
    # print(event)
