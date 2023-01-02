import smtplib
import random
import datetime as dt
import pandas

##################### Extra Hard Starting Project ######################

email = "jananpatel2002@gmail.com"
app_password = "rhgqzrjuxcqltprf"
date_time = dt.datetime.now()
amount_of_letters = 3
today_day = date_time.day
today_month = date_time.month

data = pandas.read_csv("birthdays.csv")
birthday_data_this_month = data[data.month == today_month]
birthday_data_today = birthday_data_this_month[birthday_data_this_month.day == today_day]  # Today's birthdays

today_birthday_names = [row.person_name for (index, row) in birthday_data_today.iterrows()]
index = 0
for birthday_name in today_birthday_names:
    user_email = data.email[data.index == index]  #
    random_number = random.randint(1, amount_of_letters)

    print(user_email)

    with open(f'./letter_templates/letter_{random_number}.txt', 'r') as letter_file:
        file_data = letter_file.read()
        file_data = file_data.replace("[NAME]", birthday_name)

    index += 1
    # Opens a connection for the user to send email
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.connect("smtp.gmail.com")
        connection.starttls()
        connection.login(user=email, password=app_password)
        connection.sendmail(from_addr=email, to_addrs=user_email,
                            msg=f"Subject: Happy birthday {birthday_name}!\n\n"
                                f"{file_data}")

