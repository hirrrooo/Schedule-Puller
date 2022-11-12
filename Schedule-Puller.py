# Schedule-Puller.py 
# by hirrrooo

from datetime import datetime
from pathlib import Path

import pandas as pd
from gcsa.event import Event
from gcsa.google_calendar import GoogleCalendar
from gcsa.reminders import PopupReminder

data_folder = Path('schedule')
Schedule = data_folder / 'Welcome.html'
tables = pd.read_html(Schedule)
gc = GoogleCalendar()
calendar = GoogleCalendar('iamhirojl@gmail.com')

def convert24(str1): #specially formatted to work with the schedule.
    # If element is blank, return blank.
    if str1 == '':
        return ''
    # Checking if first two elements are 12 and last two elements of time is AM 
    elif str1[:2] == "12" and str1[-2:] == "AM":
        return "00" + str1[2:-2]

    # remove the AM    
    elif str1[-2:] == "AM":
        return str1[:-3]

    # Checking if first two elements are 12 and last two elements of time is PM
    elif str1[:2] == "12" and str1[-2:] == "PM":
        return str1[:-3]

    elif len(str1) == 8:
        # add 12 to hours and remove PM
        return str(int(str1[:1]) + 12) + str1[2:8]
    else:
        str1 = ''.join(('0',str1))
        return str(int(str1[:2]) + 12) + str1[2:5]

def create_event(ShiftDay, ShiftMonth, ShiftStartTimeHour, ShiftStartTimeMinute, ShiftEndTimeHour, ShiftEndTimeMinute, Year = 2022): 
    start = datetime(year=Year, month=ShiftMonth, day=ShiftDay, hour=ShiftStartTimeHour, minute=ShiftStartTimeMinute)
    end = datetime(year=Year, month=ShiftMonth, day=ShiftDay, hour=ShiftEndTimeHour, minute=ShiftEndTimeMinute)
    event = Event('Workplace', start, end, 
    description = 'Work', 
    location = '1234 Example St, Example, NY 12345',', 
    reminders = [PopupReminder(minutes_before_start = 30), PopupReminder(minutes_before_start = 60)]
    )
    gc.add_event(event) # Comment to disable adding events to calendar.
    # todo; add color to event
    print(event)

def read_table():
    for i in range(len(shifts_dates)):
        if ShiftEndTimeHour[i] == '':
            pass
        else:
            create_event(int(ShiftDay[i]), int(ShiftMonth[i]), int(ShiftStartTimeHour[i]), int(ShiftStartTimeMinute[i]), int(ShiftEndTimeHour[i]), int(ShiftEndTimeMinute[i]))

shifts_dates = [tables[15][i][7] for i in range(2,9)] # ['Sun 10/30', 'Mon 10/31', 'Tue 11/1', 'Wed 11/2', 'Thu 11/3', 'Fri 11/4', 'Sat 11/5']
shifts = [tables[15][i][11] for i in range(2,9)] # ['9:30 AM-6:00 PM', nan, nan, nan, nan, nan, '9:00 AM-5:30 PM']
shifts = list(map(str, shifts)) # Makes every item in a list a string.
shifts = [item.replace('nan','') for item in shifts] # Replaces nan (float), with a empty string.

ShiftMonth = [i[4:6] for i in shifts_dates] # ['10', '10', '11', '11', '11', '11', '11']
ShiftDay = [i[7:] for i in shifts_dates] # ['6', '7', '8', '9', '10', '11', '12']

ShiftStartTimes = [i.split('-')[0] for i in shifts] # ['9:30 AM', '', '12:30 PM', '', '', '', '9:30 AM']
ShiftStartTimes = [convert24(times) for times in ShiftStartTimes] # same thing as above but in 24hr format
ShiftStartTimeHour = [i.split(':')[0] for i in ShiftStartTimes] # ['9', '', '12', '', '', '', '9']
ShiftStartTimeMinute = [i.split(':')[1] if len(i) > 0  else "" for i in ShiftStartTimes] # ['30', '', '30', '', '', '', '30']

ShiftEndTimes =  [i.split('-')[1] if len(i) > 0  else "" for i in shifts] # ['6:00 PM', '', '8:00 PM', '', '', '', '6:00 PM']
ShiftEndTimes = [convert24(times) for times in ShiftEndTimes] # same thing as above but in 24hr format
ShiftEndTimeHour = [i.split(':')[0] for i in ShiftEndTimes]
ShiftEndTimeMinute = [i.split(':')[1] if len(i) > 0  else "" for i in ShiftEndTimes]

read_table()