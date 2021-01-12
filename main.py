import schedule
import time
import webbrowser as wb
import os

# Custom list of meetings as dictionaries
from config import meetings

# Joins a class for the specified meeting duration.
def joinClass(zoom_link, meeting_duration):
    wb.get(using='firefox').open(zoom_link, new=2)
    time.sleep(5)
   
    print("Session has started and will continue for %s minutes" % meeting_duration)

    print('Hold (Ctrl+c) to exit the program ')

    # Total time of zoom session
    time.sleep(meeting_duration * 60)

    # Close Zoom (this part is Mac OS-specific)
    os.system("pkill -f zoom")
    time.sleep(0.5)

for meeting in meetings:
    schedule.every().day.at("%s" % meeting['time']).do(lambda: joinClass(meeting['link'], meeting['duration']))
    print(f"Scheduling {meeting['name']} every day at {meeting['time']}")


# Infinite Loop so that the scheduled task keeps running
while True:
    # Check whether a scheduled task is pending to run or not
    schedule.run_pending()
    time.sleep(30)