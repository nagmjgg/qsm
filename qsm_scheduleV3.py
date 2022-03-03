"""
https://www.geeksforgeeks.org/python-schedule-library/
https://schedule.readthedocs.io/en/stable/

Remember to install pandas in current
V3 Logging to mysql implemented
    update parts 3/2/22

"""

import mysql.connector
import pandas as pd
import time
# Schedule Library imported
import subprocess
import schedule
import logging
from datetime import date,datetime
#from qsm_functions import *
#from postgresql_connectionV1_3 import update_table_combined_inventory

def create_table_from_csv_replace(table_name, csv_filename):

   df = pd.read_csv(csv_filename)
   df.columns = [c.lower() for c in df.columns]  # postgres doesn't like capitals or spaces

   from sqlalchemy import create_engine
   engine = create_engine('postgresql://' + username + ':' + user_password + '@localhost:5432/' + db_name + '')
   print(engine)
   df.to_sql(table_name, engine, if_exists='replace')
   print(f"exporting file > {csv_filename}")

def update_table_combined_inventory():
   filename_combined = find_last_file('D:/shared_inventory/server files/', 'Combined_')
   print(f"importing file > {filename_combined}")
   create_table_from_csv_replace('onhand_ingredients',filename_combined)

def date_now():
    date = datetime.now().strftime("%Y-%m-%d")
    return date

def time_now():
    time = datetime.now().strftime("%H:%M")
    return time

def log(message_text,  level):
    global script_name
    date_log = date_now()
    time_log = time_now()

    query = "insert into logs (date, time, script_name, text, level) values (%s, %s, %s, %s, %s)"

    cursor.execute(query, (date_log, time_log, script_name, message_text, level))
    conn.commit()

folder = 'D:/shared_inventory/server files/'

# Functions setup
def qsm_merge():
    print("Executing Merge...")
    subprocess.call(["python","qsm_mergeV4_3.py"])
    log("qsm_merge ok","info")

def update_parts():
    print("Updating Parts...")
    subprocess.call(["python","qsm_update_parts V1.py"])
    log("'parts' updated ok","info")


# Task scheduling
# After every 10mins geeks() is called.
#schedule.every(10).minutes.do(geeks)

# After every hour geeks() is called.
#schedule.every().hour.do(geeks)

# After every 5 to 10mins in between run work()
#schedule.every(5).to(10).minutes.do(work)

# Every monday good_luck() is called
#schedule.every().monday.do(good_luck)

# Every monday good_luck() is called - TEST
#schedule.every().day.at("12:30").do(good_luck)

# Every tuesday at 18:00 sudo_placement() is called
#schedule.every().tuesday.at("18:00").do(work)



# Every day at 7 am or 00:00 time bedtime() is called.
schedule.every().day.at("07:10").do(qsm_merge)

# Every day at 7 am or 00:00 time bedtime() is called.
schedule.every().day.at("07:10").do(update_parts)

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

# Loop so that the scheduling task
# keeps on running all time.
while True:
    # Checks whether a scheduled task
    # is pending to run or not
    schedule.run_pending()
    time.sleep(1)