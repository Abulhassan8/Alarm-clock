from tkinter import *
import datetime
import time
import pytz

def alarm(set_alarm_timer):
    while True:
        time.sleep(1)
        current_time=datetime.datetime.now(pytz.timezone('Asia/Kolkata'))
        now=current_time.strftime("%I:%M:%S")
        date=current_time.strftime("%d/%m/%Y")
        print("The set date is : ",date)
        if now==set_alarm_timer:
            print("Time to wakeup")
            break
def present_time():
    return (time.strftime("%I:%M:%S"))
if __name__=='__main__':
    current_time = datetime.datetime.now(pytz.timezone('Asia/Kolkata'))
    while(1):
        print('{}\r'.format(present_time()), end="")
        continue


    hour=input("Enter hour: ")
    minute=input("Enter minutes: ")
    seconds=input("Enter seconds: ")
    set_alarm_timer="{}:{}:{}".format(hour,minute,seconds)
    alarm(set_alarm_timer)