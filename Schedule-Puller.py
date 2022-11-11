# Schedule-Puller.py 
# by hirrrooo

import pandas as pd
from gcsa.event import Event
from gcsa.google_calendar import GoogleCalendar
from gcsa.recurrence import Recurrence, DAILY, SU, SA
from datetime import date, datetime
from pathlib import Path
import numpy as np
from beautiful_date import *


data_folder = Path('schedule')
Schedule = data_folder / 'Welcome.html'
tables = pd.read_html(Schedule)

shifts_dates = [tables[15][i][7] for i in range(2,9)] # ['Sun 10/30', 'Mon 10/31', 'Tue 11/1', 'Wed 11/2', 'Thu 11/3', 'Fri 11/4', 'Sat 11/5']
shifts = [tables[15][i][11] for i in range(2,9)] # ['9:30 AM-6:00 PM', nan, nan, nan, nan, nan, '9:00 AM-5:30 PM']
shifts = list(map(str, shifts)) # Makes every item in a list a string.
shifts = [item.replace('nan', '') for item in shifts] # Replaces nan (float), with a empty string.
zipped = [list(i) for i in zip(shifts_dates, shifts)] # [['Sun 10/30', '9:30 AM-6:00 PM'], ['Mon 10/31', nan], ['Tue 11/1', nan], ['Wed 11/2', nan], ['Thu 11/3', nan], ['Fri 11/4', nan], ['Sat 11/5', '9:00 AM-5:30 PM']]


def convert24(str1):
    # if element is blank, return blank.
    # Checking if last two elements of time
    # is AM and first two elements are 12
    if str1 == '':
        return ''

    elif str1[-2:] == "AM" and str1[:2] == "12":
        return "00" + str1[2:-2]
         
    # remove the AM    
    elif str1[-2:] == "AM":
        return str1[:-2]
     
    # Checking if last two elements of time
    # is PM and first two elements are 12
    elif str1[-2:] == "PM" and str1[:2] == "12":
        return str1[:-2]
         
    else:
        # add 12 to hours and remove PM
        return str(int(str1[:2]) + 12) + str1[2:8]

ShiftStartTimes = [i.split('-')[0] for i in shifts]
ShiftStartTimes = [convert24(times) for times in ShiftStartTimes]
print(ShiftStartTimes)

# ShiftEndTimes = [i.split('-')[0] for i in shifts]

def create_event(month, day, hour, minute, year = 2022):
    start = (month, day, hour, minute, year))
    end = (datetime(month, day, hour, minute, year))
    event = Event('Meeting',
                start=start,
                end=end)

# from beautiful_date import *
# d = 25/Mar/2018
# t = (25/Mar/2018)[23:45]