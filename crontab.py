# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 07:51:48 2021

@author: mgarcia
"""

from crontab import CronTab

# user=True denotes the current user
cron = CronTab(user=True)
job = cron.new(command='PGPASSWORD=test psql -U someuser -d somedb -c "SELECT 1" -h localhost')
job.setall("*/5 * * * *")

if cron[0].is_valid():  # If syntax is valid, write to crontab
    cron.write()

# crontab -l  # Check real crontab from shell
# */5 * * * * PGPASSWORD=test psql -U someuser -d somedb -c "SELECT 1" -h localhost


''' OTRO EJEMPLO

with CronTab(user='root') as cron:  # with context manager cron.write() is called automatically
    job = cron.new(
        command='PGPASSWORD=test pg_dump -U someuser -d somedb -h localhost --column-inserts --data-only > backup.sql',
        comment="Perform database backup"
    )
    job.every(2).days()
    job.hour.on(1)

    # job.every_reboot()
    # job.hour.every(10)
    # job.month.during('JAN', 'FEB')  # Powerful but confusing/hard to parse syntax
    # job.minute.during(15, 45).every(5)

# crontab -l
# 0 1 */2 * * PGPASSWORD=test pg_dump -U someuser -d somedb -h localhost --column-inserts --data-only > backup.sql # Perform database backup
'''


''' MANAGEMENT OF CRONTABS
from crontabs import CronTabs

for cron in CronTabs():  # Get list of all user and system crontabs
    if cron.user:
        print(f'{cron.user} has following cron jobs:')
    else:
        print(f'{cron.filen} has following cron jobs:')
    for job in cron.crons:
        print(f'   {job.command}')

# martin has following cron jobs:
#    PGPASSWORD=test psql -U someuser -d somedb -c "SELECT 1" -h localhost
#    PGPASSWORD=test pg_dump -U someuser -d somedb -h localhost --column-inserts --data-only > backup.sql
# /etc/cron.d/anacron has following cron jobs:
#    [ -x /etc/init.d/anacron ] && if [ ! -d /run/systemd/system ]; then /usr/sbin/invoke-rc.d anacron start >/dev/null; fi
# /etc/cron.d/popularity-contest has following cron jobs:
#    test -x /etc/cron.daily/popularity-contest && /etc/cron.daily/popularity-contest --crond
# ...

jobs = CronTabs().all.find_command('psql')  # lookup for all jobs running specific command

for job in jobs:
    print(job)

# */5 * * * * PGPASSWORD=test psql -U someuser -d somedb -c "SELECT 1" -h localhost
'''