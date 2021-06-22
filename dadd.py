#!/usr/bin/env python3

import subprocess
from subprocess import PIPE


# Lists with allowed values

month_list = ['jan', 'feb', 'mar', 'apr', 'may', 'june', 'july', 'aug', 'sept', 'oct', 'nov', 'dec', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun', "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]

day_list = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun', "0", "1", "2", "3", "4", "5", "6"]


# Current user information

uinfo = subprocess.run('whoami', capture_output=True, text=True)
duinfo = uinfo.stdout.strip()
print('-'*30)

# ADD

try:
    # MINUTES while loop

    while True:
        try:
            minutes = input('> Input minutes (0-59): ')
            if int(minutes) >= 0 and int(minutes) <= 59:
                print('- Accepted -')
                break
            else:
                print('The number has to be between 0 and 59!')
        except ValueError:
            print('-- * is added instead! --')
            minutes = '*'
            break

    # HOURS while loop

    while True:
        try:
            hours = input('> Input hours (0-23): ')
            if int(hours) >= 0 and int(hours) <= 23:
                print('- Accepted -')
                break
            else:
                print('The number has to be between 0 and 23!')
        except ValueError:
            print('-- * is added instead! --')
            hours = '*'
            break

    # DayOfMonth while loop

    while True:
        try:
            dom = input('> Input day of month: (1-31): ')
            if int(dom) >= 1 and int(dom) <= 31:
                print('- Accepted -')
                break
            else:
                print('The number has to be between 1 and 31!')
        except ValueError:
            print('-- * is added instead! --')
            dom = '*'
            break

    # MONTHS while loop

    while True:
        try:
            months = input('> Input a month (1-12 or jan-dec): ')

            if months in month_list:
                print('- Accepted -')
                break
            else:
                print('Enter either 1-12 or jan-dec!')
        except ValueError:
            print('-- * is added instead! --')
            months = '*'
            break


    # DayOfWeek while loop

    while True:
        try:
            dow = input('> Input a day of the week (0-6 or sun-sat): ')

            if dow in day_list:
                print('- Accepted -')
                break
            else:
                print('Enter either 0-6 or sun-sat!')
        except ValueError:
            print('-- * is added instead! --')
            months = '*'
            break

    # TASK variable
    while True:
        try:
            task = input('> Cron will do: ')
            if task == '' or task == ' ':
                print('- Cannot leave this empty! -')
            else:
                break
        except ValueError:
            print('You didn\'t do something correctly.')
            break

    # Ask whether or not to save the cron job

    print('-'*30)
    docron = '(crontab -l ; echo "%s %s %s %s %s   %s") | crontab - \n' % (
        minutes, hours, dom, months, dow, task)
    view_docron = '%s %s %s %s %s   %s' % (
        minutes, hours, dom, months, dow, task)
    print('> This is your new cron job: \n')
    print(view_docron)
    print('-'*30)
    while True:
        try:
            answer = input(
                '> Do you want to save it, %s? \nType "no" to DISCARD or press Enter to SAVE: \n>> ' % duinfo)
            if answer.lower() == 'no' or answer.lower() == 'n':
                print('-'*30)
                print('The cron job has been DISCARDED!')
                print('-'*30)
                break
            else:
                p1 = subprocess.run('%s' % docron, shell=True,
                                        stderr=subprocess.DEVNULL, stdout=PIPE)
                print('-'*30)
                print('-- Success --')
                print('-'*30)
                break
        except ValueError:
            print('Error occured!')
except:
    print('\n' + '-'*30)
    print('> User %s ended the program!' % duinfo)
    print('-'*30)


