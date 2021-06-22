#!/usr/bin/env python3

import subprocess
from subprocess import PIPE
import time

uinfo = subprocess.run('whoami', capture_output=True, text=True)
duinfo = uinfo.stdout.strip()
print('-'*30)


# Take the command

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


# Present options
print('-'*30)
time.sleep(0.5)

print('@yearly')
print('@monthly')
print('@weekly')
print('@daily')
print('@hourly')
print('@reboot\n')
print('Don\'t forget to include the leading "@" symbol!')
print('-'*30)

while True:
    try:
        # User choice
        asked = input('> Which one will you choose, %s: ' % duinfo)

        # @yearly
        if asked == "@yearly" or asked == "@annually":
            print('-'*30)
            print('> Congrats! This is your new cron job: \n')
            view_docron = '%s   %s' % (asked, task)
            print(view_docron)
            print('-'*30)
            break
        else:
            # @monthly
            if asked == "@monthly":
                print('-'*30)
                print('> Congrats! This is your new cron job: \n')
                view_docron = '%s   %s' % (asked, task)
                print(view_docron)
                print('-'*30)
                break
            else:
                # @weekly
                if asked == "@weekly":
                    print('-'*30)
                    print('> Congrats! This is your new cron job: \n')
                    view_docron = '%s   %s' % (asked, task)
                    print(view_docron)
                    print('-'*30)
                    break
                else:
                    # @daily
                    if asked == "@daily":
                        print('-'*30)
                        print('> Congrats! This is your new cron job: \n')
                        view_docron = '%s   %s' % (asked, task)
                        print(view_docron)
                        print('-'*30)
                        break  
                    else:
                        # @hourly
                        if asked == "@hourly":
                            print('-'*30)
                            print('> Congrats! This is your new cron job: \n')
                            view_docron = '%s   %s' % (asked, task)
                            print(view_docron)
                            print('-'*30)
                            break 
                        else:
                            # @reboot
                            if asked == "@reboot":
                                print('-'*30)
                                print('> Congrats! This is your new cron job: \n')
                                view_docron = '%s   %s' % (asked, task)
                                print(view_docron)
                                print('-'*30)
                                break
                            else:
                                print('-'*30)
                                print('-- Use your brain, %s --' % duinfo)
                                print('-'*30)
    except:
        print('\n' + '-'*30)
        print('> User %s ended the program!' % duinfo)
        print('-'*30)
        break


docron = '(crontab -l ; echo "%s") | crontab - \n' % view_docron

#print(docron)

p1 = subprocess.run('%s' % docron, shell=True,
                        stderr=subprocess.DEVNULL, stdout=PIPE)

