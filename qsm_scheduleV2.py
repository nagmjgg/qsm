"""
https://www.geeksforgeeks.org/python-schedule-library/
https://schedule.readthedocs.io/en/stable/

Remember to install pandas in current
"""

import pandas as pd
import time
# Schedule Library imported
import subprocess
import schedule
import logging
#from qsm_functions import *
#from postgresql_connectionV1_3 import update_table_combined_inventory

def update_table_combined_inventory():
   filename_combined = find_last_file('D:/shared_inventory/server files/', 'Combined_')
   print(f"importing file > {filename_combined}")
   create_table_from_csv_replace('onhand_ingredients',filename_combined)




#logging.basicConfig(filename='schedule_loging.log', encoding='utf-8', level=logging.DEBUG)
"""
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')
logging.error('And non-ASCII stuff, too, like Øresund and Malmö')
"""
folder = 'D:/shared_inventory/server files/'

root_logger = logging.getLogger()
root_logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(folder + 'qsm_logfile.log', 'w', 'utf-8')
root_logger.addHandler(handler)

logging.basicConfig(level=logging.INFO, format='%(asctime)s :: %(levelname)s :: %(message)s')
formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s',
                              '%m-%d-%Y %H:%M:%S')
logging.warning('The Admin just logged out')

# Functions setup
def qsm_merge():
    print("Executing Merge...")
    subprocess.call(["python","qsm_mergeV4_3.py"])
    logging.info('qsm_merge ok')

def good_luck():
    print("Good Luck for Test")
    logging.warning('The Admin just logged out')

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

# Every day at 9 am or 00:00 time bedtime() is called.
schedule.every().day.at("09:10").do(qsm_merge)

# Every day at 11 am or 00:00 time bedtime() is called.
schedule.every().day.at("11:10").do(qsm_merge)

# Every day at 2 pm or 00:00 time bedtime() is called.
schedule.every().day.at("14:10").do(qsm_merge)

# Every day at 2 pm or 00:00 time bedtime() is called.
schedule.every().day.at("07:18").do(qsm_merge)

# Every day at 7am or 00:00 time bedtime() is called.
schedule.every().day.at("07:10").do(update_table_combined_inventory)

# Every day at 9am or 00:00 time bedtime() is called.
schedule.every().day.at("09:10").do(update_table_combined_inventory)

# Every day at 11 am or 00:00 time bedtime() is called.
schedule.every().day.at("11:10").do(update_table_combined_inventory)

# Every day at 2 pm or 00:00 time bedtime() is called.
schedule.every().day.at("14:10").do(update_table_combined_inventory)

# Every day at 7am or 00:00 time bedtime() is called.
schedule.every().day.at("07:18").do(update_table_combined_inventory)

# After every 5 to 10mins in between run work()
schedule.every(5).to(10).minutes.do(work)

# Every monday good_luck() is called
schedule.every().monday.do(good_luck)

# Every monday good_luck() is called - TEST
schedule.every().day.at("12:30").do(good_luck)

# Every tuesday at 18:00 sudo_placement() is called
schedule.every().tuesday.at("18:00").do(work)

# Loop so that the scheduling task
# keeps on running all time.
while True:
    # Checks whether a scheduled task
    # is pending to run or not
    schedule.run_pending()
    time.sleep(1)