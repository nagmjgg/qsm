"""
https://www.geeksforgeeks.org/python-schedule-library/
https://schedule.readthedocs.io/en/stable/

Remember to install pandas in current
"""

import time
# Schedule Library imported
import subprocess
import schedule
#import logging
from qsm_functions import *
from postgresql_connectionV1_3 import update_table_combined_inventory


#logging.basicConfig(filename='schedule_loging.log', encoding='utf-8', level=logging.DEBUG)
"""
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')
logging.error('And non-ASCII stuff, too, like Øresund and Malmö')
"""

# Functions setup
def qsm_merge():
    print("Executing Merge...")
    subprocess.call(["python","qsm_mergeV4_3.py"])
    logging.info('qsm_merge ok')

def good_luck():
    print("Good Luck for Test")


def work():
    print("Study and work hard")


def bedtime():
    print("It is bed time go rest")


def geeks():
    print("Shaurya says Geeksforgeeks")


# Task scheduling
# After every 10mins geeks() is called.
schedule.every(10).minutes.do(geeks)

# After every hour geeks() is called.
schedule.every().hour.do(geeks)

# Every day at 7 am or 00:00 time bedtime() is called.
schedule.every().day.at("07:10").do(qsm_merge)

# Every day at 11 am or 00:00 time bedtime() is called.
schedule.every().day.at("11:10").do(qsm_merge)

# Every day at 2 pm or 00:00 time bedtime() is called.
schedule.every().day.at("14:10").do(qsm_merge)

# Every day at 7am or 00:00 time bedtime() is called.
schedule.every().day.at("07:10").do(update_table_combined_inventory)

# Every day at 11 am or 00:00 time bedtime() is called.
schedule.every().day.at("11:10").do(update_table_combined_inventory)

# Every day at 2 pm or 00:00 time bedtime() is called.
schedule.every().day.at("14:10").do(update_table_combined_inventory)


# After every 5 to 10mins in between run work()
schedule.every(5).to(10).minutes.do(work)

# Every monday good_luck() is called
schedule.every().monday.do(good_luck)

# Every tuesday at 18:00 sudo_placement() is called
schedule.every().tuesday.at("18:00").do(work)

# Loop so that the scheduling task
# keeps on running all time.
while True:
    # Checks whether a scheduled task
    # is pending to run or not
    schedule.run_pending()
    time.sleep(1)