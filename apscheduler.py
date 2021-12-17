# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 08:11:41 2021

@author: mgarcia

url> https://apscheduler.readthedocs.io/en/3.x/userguide.html
"""

jobstores = {
    'mongo': MongoDBJobStore(),  # MongoDBJobStore requires PyMongo installed - `pip install pymongo`
    'default': SQLAlchemyJobStore(url='sqlite:///jobs.sqlite')  # SQLAlchemyJobStore requires SQLAlchemy installed, Recommended to use PostgreSQL
}
executors = {
    'default': ThreadPoolExecutor(20),
    'processpool': ProcessPoolExecutor(5)
}
job_defaults = {
    'coalesce': False,
    'max_instances': 3
}
scheduler = BackgroundScheduler(jobstores=jobstores,
                                executors=executors,
                                job_defaults=job_defaults,
                                timezone=utc,
                                daemon=True)  # Without daemonic mode, the main thread would exit. You can also keep it alive with infinite loop.

def task():
    return ...

# trigger -> can also be 'cron' or 'date'
# misfire_grace_time -> seconds after the designated runtime that the job is still allowed to be run
# max_instances -> max number of concurrent instances
scheduler.add_job(task, trigger='interval', seconds=5, misfire_grace_time=600, max_instances=5)
# 'interval' trigger can take any args from https://apscheduler.readthedocs.io/en/latest/modules/triggers/interval.html#module-apscheduler.triggers.interval

scheduler.add_job(task, trigger='cron', month='jan-apr', day_of_week='mon-fri', hour=15, minute=30, end_date='2021-01-30')
scheduler.add_job(task, CronTrigger.from_crontab('0 17 * * sat,sun'))
# 'cron' trigger can take any args from https://apscheduler.readthedocs.io/en/latest/modules/triggers/cron.html#module-apscheduler.triggers.cron

# Simulates 'at' - deferred jobs
scheduler.add_job(task, trigger='date', run_date=datetime(2020, 12, 24, 17, 30, 0))
# 'date' trigger can take any args from https://apscheduler.readthedocs.io/en/latest/modules/triggers/date.html#module-apscheduler.triggers.date

scheduler.print_jobs(jobstore="default")

scheduler.start()

# Pending jobs:
#     task (trigger: interval[0:01:00], pending)
#     task (trigger: cron[month='jan-apr', day_of_week='mon-fri', hour='15', minute='30'], pending)
#     task (trigger: cron[month='*', day='*', day_of_week='sat,sun', hour='17', minute='0'], pending)
#     task (trigger: date[2020-12-24 17:30:00 UTC], pending)


'''
# Catching scheduler events:
import logging

logging.basicConfig(level=logging.INFO)

def my_listener(event):
    if event.exception:
        logging.warning('Job failed...')
    else:
        logging.info('Job was executed...')


scheduler.add_listener(my_listener, EVENT_JOB_EXECUTED | EVENT_JOB_ERROR)

# ...
# INFO:apscheduler.scheduler:Scheduler started
# INFO:apscheduler.executors.default:Running job "task (trigger: interval[0:00:05], next run at: 2020-10-30 09:51:11 UTC)" (scheduled at 2020-10-30 09:51:11.222311+00:00)
# INFO:apscheduler.executors.default:Job "task (trigger: interval[0:00:05], next run at: 2020-10-30 09:51:16 UTC)" executed successfully
# INFO:root:Job was executed...
'''

