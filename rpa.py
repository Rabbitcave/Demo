import pywhatkit as kit
openwhatsapp = kit.open_whatsapp()
# WhatsApp number (include country code)
phone_number = "+918973040394"  # Replace with recipient's number

# Message to send
message = "Hello! This is a scheduled message from Python on 3rd July 2025 at 1:50 PM 🕐"

# Scheduled date and time
year = 2025
month = 7
day = 3
hour = 13     # 1 PM is 13 in 24-hour format
minute = 50   # 50 minutes

import time
from datetime import datetime

print("WhatsApp message scheduled successfully for 3rd July 2025 at 1:50 PM.")
scheduled_datetime = datetime(year, month, day, hour, minute)
while datetime.now() < scheduled_datetime:
	time.sleep(30)  # Check every 30 seconds

# Send the message
kit.sendwhatmsg(phone_no=phone_number, message=message, time_hour=hour, time_min=minute, wait_time=5, tab_close=True, close_time=3)

print("Hi this is hari.")
