"""
Demonstrates how to schedule a job to be run in a process pool on 3 second intervals.

https://programmer.group/python-uses-apscheduler-for-timed-tasks.html

another example :

from datetime import datetime
from datetime import date
from apscheduler.schedulers.blocking import BlockingScheduler

def job(text):
    print(text)

scheduler = BlockingScheduler()
# In 2019-8-30 Run once job Method
scheduler.add_job(job, 'date', run_date=date(2019, 8, 30), args=['text1'])
# In 2019-8-30 01:00:00 Run once job Method
scheduler.add_job(job, 'date', run_date=datetime(2019, 8, 30, 1, 0, 0), args=['text2'])
# In 2019-8-30 01:00:01 Run once job Method
scheduler.add_job(job, 'date', run_date='2019-8-30 01:00:00', args=['text3'])

scheduler.start()

***************

Trigger interval

Fixed interval trigger.The parameters are as follows:

parameter	Explain
weeks (int)	Weeks apart
days (int)	A few days apart
hours (int)	Hours apart
minutes (int)	Minutes apart
seconds (int)	How many seconds apart
start_date (datetime or str)	Start date
end_date (datetime or str)	End date
timezone (datetime.tzinfo or str)

example2

import time
from apscheduler.schedulers.blocking import BlockingScheduler

def job(text):
    t = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    print('{} --- {}'.format(text, t))

scheduler = BlockingScheduler()
# Run every minute job Method
scheduler.add_job(job, 'interval', minutes=1, args=['job1'])
# In 2019-08-29 22:15:00 To 2019-08-29 22:17:00 Period, run every 1 minute 30 seconds job Method
scheduler.add_job(job, 'interval', minutes=1, seconds = 30, start_date='2019-08-29 22:15:00', end_date='2019-08-29 22:17:00', args=['job2'])

scheduler.start()

'''
//Run result:
job2 --- 2019-08-29 22:15:00
job1 --- 2019-08-29 22:15:46
job2 --- 2019-08-29 22:16:30
job1 --- 2019-08-29 22:16:46
job1 --- 2019-08-29 22:17:46
...Remaining omitted...
'''

Trigger cron

Triggers periodically at a specific time.The parameters are as follows:

parameter	Explain
year (int or str)	Year, 4 digits
month (int or str)	Month (range 1-12)
day (int or str)	Days (range 1-31)
week (int or str)	Weeks (range 1-53)
day_of_week (int or str)	The day or day of the week (range 0-6 or mon,tue,wed,thu,fri,sat,sun)
hour (int or str)	Hour (range 0-23)
minute (int or str)	Score (range 0-59)
second (int or str)	Seconds (range 0-59)
start_date (datetime or str)	Earliest start date (inclusive)
end_date (datetime or str)	Latest end time (inclusive)
timezone (datetime.tzinfo or str)	Specify time zone

expression  field   description
*           any     fire on every value
*/a         any     fire every a values, starting from the minimum
a-b         any     fire on any value within the a-b range (a must be smaller than b)
a-b/c       any     fire every c values within the a-b range
xth y       day     fire on the x -th occurrence of weekday y within the month
last x      day     fire on the last occurrence of weekday x within the month
last        day     fire on the las day within the month
x,y,z       any     fire on any matching expression; can combine any number of any of the above expressions

example 3

import time
from apscheduler.schedulers.blocking import BlockingScheduler

def job(text):
    t = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    print('{} --- {}'.format(text, t))

scheduler = BlockingScheduler()
# Run every minute at 22 o'clock a day job Method
scheduler.add_job(job, 'cron', hour=22, minute='*/1', args=['job1'])
# Run once a day at 22 and 23:25 job Method
scheduler.add_job(job, 'cron', hour='22-23', minute='25', args=['job2'])

scheduler.start()

'''
//Run result:
job1 --- 2019-08-29 22:25:00
job2 --- 2019-08-29 22:25:00
job1 --- 2019-08-29 22:26:00
job1 --- 2019-08-29 22:27:00
...Remaining omitted...


example 4>

Add method by decorator scheduled_job()

There are two ways to add tasks:

(1) By calling add_job() - see codes 1 to 3 above
(2) through the decorator scheduled_job():
The first is the most common method.The second method is primarily to conveniently declare tasks that will not change when the application is running.The add_job() method returns an apscheduler.job.Job instance that you can use to modify or delete the task later.

import time
from apscheduler.schedulers.blocking import BlockingScheduler

scheduler = BlockingScheduler()

@scheduler.scheduled_job('interval', seconds=5)
def job1():
    t = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    print('job1 --- {}'.format(t))

@scheduler.scheduled_job('cron', second='*/7')
def job2():
    t = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    print('job2 --- {}'.format(t))

scheduler.start()

'''
//Run result:
job2 --- 2019-08-29 22:36:35
job1 --- 2019-08-29 22:36:37
job2 --- 2019-08-29 22:36:42
job1 --- 2019-08-29 22:36:42
job1 --- 2019-08-29 22:36:47
job2 --- 2019-08-29 22:36:49
...Remaining omitted...
'''



"""

from datetime import datetime
import os

from apscheduler.schedulers.blocking import BlockingScheduler


def tick():
    print('Tick! The time is: %s' % datetime.now())

def tock():
    print('Tock! The time is: %s' % datetime.now())

if __name__ == '__main__':
    scheduler = BlockingScheduler()
    scheduler.add_executor('processpool')
    scheduler.add_job(tick, 'interval', seconds=10)
    scheduler.add_job(tock, 'interval', seconds=5)
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))

    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        pass