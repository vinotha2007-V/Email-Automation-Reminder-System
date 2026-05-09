import schedule
import time
import reminder

def job():
    print("Checking reminders...")
    import reminder

schedule.every(1).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
