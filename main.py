##################### Extra Hard Starting Project ######################
import datetime as dt
import smtplib

import pandas as pd
import smtplib as st
import random as r
# 1. Update the birthdays.csv
data_file = pd.read_csv('birthdays.csv')

# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
year = now.year
month = now.month
day = now.day

today_date_raw = f'{year}/{month}/{day}'
format_string = "%Y/%m/%d"


today_date = dt.datetime.strptime(today_date_raw, format_string)

data_file['date'] = pd.to_datetime(data_file[['year', 'month', 'day']])
birthday = None


for date in data_file['date']:
    if date == today_date:
        birthday = date


#getting index of name
index_of_target_date = data_file[data_file['date'] == birthday].index
name = data_file['name'].iloc[index_of_target_date[0]]
#Getting index of email
email = data_file['email'].iloc[index_of_target_date[0]]



# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv


if birthday != None:
    number = r.randint(1,3)
    with open(f'./letter_templates/letter_{number}.txt') as letter_file:
        contents = letter_file.read()
        updated_content = contents.replace("[NAME]", name)
        print(updated_content)


# 4. Send the letter generated in step 3 to that person's email address.
my_email = "example@gmail.com"
my_password = "APP PASS HERE"
connection = smtplib.SMTP('smtp.gmail.com')
connection.starttls()
connection.login(user=my_email,password=my_password)
connection.sendmail(from_addr=my_email,to_addrs=email,msg=f'Subject:Happy Birthday!\n\n{updated_content}')
connection.close()



