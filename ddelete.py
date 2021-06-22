#!/usr/bin/env python3

import subprocess

#DELETE


print('-'*30)
user = input('> Do you really want to delete ALL cron jobs?\nType "yes" to remove or Enter to stop this action: ')
print('-'*30)
if user.lower() == 'yes':
    remove = subprocess.run('crontab -d || crontab -r', capture_output=True, shell=True, text=True)
    print('Cron jobs have been DELETED!')
    print('-'*30)
else:
    print('No cron jobs have been hurt.')
    print('-'*30)






