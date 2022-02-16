def log(message_text,  level):
    global script_name
    date_log = date_now()
    time_log = time_now()

    query = "insert into logs (date, time, script_name, text, level) values (%s, %s, %s, %s, %s)"

    cursor.execute(query, (date_log, time_log, script_name, message_text, level))
    conn.commit()