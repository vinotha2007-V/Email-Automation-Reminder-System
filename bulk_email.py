import pandas as pd
from main import send_email

contacts = pd.read_csv("contacts.csv")

with open("templates/email_template.txt") as file:
    template = file.read()

for index, row in contacts.iterrows():
    name = row["name"]
    email = row["email"]

    message = template.format(name=name)

    send_email(
        email,
        "Automated Bulk Email",
        message
    )
