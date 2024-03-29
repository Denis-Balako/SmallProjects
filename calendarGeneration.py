#! python3

""""Calendar maker, Denis Balako denisarius2000s
Tags: short"""

import datetime

DAYS = ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday',
        'Friday', 'Saturday')
MONTHS = ('January', 'February', 'March', 'April', 'May',
          'June', 'July', 'August', 'September', 'October',
          'November', 'December')

print('Calendar maker, by Denis Balako denisarius2000s@gmail.com')

while True:  # Ask year
    print('Enter the year of calendar:')
    response = input('> ')

    if response.isdecimal() and int(response) > 0:
        year = int(response)
        break

    print('Please, enter the numeric year, like 2023.')

while True:  # Ask month
    print('Enter the month of the calendar, 1-12:')
    response = input('> ')

    if not response.isdecimal():
        print('Please, enter the numeric month, like 3 for March.')
        continue

    month = int(response)
    if 1 <= month <= 12:
        break

    print('Please, enter a number from 1 to 12.')


def getCalendarFor(year, month):
    calText = ''

    calText += (' ' * 34) + MONTHS[month - 1] + ' ' + str(year) + '\n'
    calText += '...Sunday.....Monday....Tuesday...Wednesday...'
    calText += 'Thursday....Friday....Saturday..\n'

    weekSeparator = ('+----------' * 7) + '+\n'
    blankRow = ('|          ' * 7) + '|\n'

    currentDate = datetime.date(year, month, 1)
    while currentDate.weekday() != 6:
        currentDate -= datetime.timedelta(days=1)

    while True:
        calText += weekSeparator

        dayNumberRow = ''
        for i in range(7):
            DayNubmerLabel = str(currentDate.day).rjust(2)
            dayNumberRow += '|' + DayNubmerLabel + (' ' * 8)
            currentDate += datetime.timedelta(days=1)
        dayNumberRow += '|\n'
        calText += dayNumberRow
        for i in range(3):
            calText += blankRow

        if currentDate.month != month:
            break

    calText += weekSeparator
    return calText


calText = getCalendarFor(year, month)
print(calText)

calendarFileName = 'calendar_{}_{}.txt'.format(year, month)
with open(calendarFileName, 'w') as fileObj:
    fileObj.write(calText)

print('Saved to ' + calendarFileName)
