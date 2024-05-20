import pywhatkit

# Take user input for hour and minute
try:
    hour = int(input("Enter hour (24-hour format, 0-23): "))
    minute = int(input("Enter minute (0-59): "))

    # Ensure the hour and minute are within valid ranges
    if (hour < 0 or hour > 23) or (minute < 0 or minute > 59):
        print("Invalid time entered. Please enter a valid hour (0-23) and minute (0-59).")
    else:
        # Send WhatsApp message
        pywhatkit.sendwhatmsg("+917489356891", "Hi this is Bhupesh", hour, minute)
        print("Message scheduled successfully.")

except ValueError:
    print("Invalid input. Please enter numerical values for hour and minute.")
