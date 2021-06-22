#!/usr/bin/env python3

import subprocess


# View active cron jobs

cron = subprocess.run('crontab -l', capture_output=True, text=True, shell=True)
if cron.returncode >= 1:
    print('-'*30)
    print('There are no cron jobs!')
    print('-'*30)

else:
    print('-'*30)
    print(cron.stdout)
    print('-'*30)



