import datetime
import time
import os

alarm_time = input("Set alarm time (HH:MM:SS): ")
alarm_hour, alarm_minute, alarm_second = map(int, alarm_time.split(":"))

print("Alarm set...")

while True:
    now = datetime.datetime.now()
    if (now.hour == alarm_hour and 
        now.minute == alarm_minute and 
        now.second == alarm_second):
        print("Wake up!")
        
        break
    time.sleep(1)
