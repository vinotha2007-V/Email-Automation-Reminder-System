import pandas as pd
from datetime import datetime
from main import send_email

reminders = pd.read_csv("reminders.csv")

current_time = datetime.now().strftime("%H:%M")

for index, row in reminders.iterrows():

    if row["time"] == current_time:

        send_email(
            row["email"],
            "Reminder Notification",
            row["message"]
        )

        print("Reminder sent!")
