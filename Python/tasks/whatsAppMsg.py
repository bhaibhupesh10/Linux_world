import pywhatkit as kit

# Specify the recipient's phone number (including country code, e.g., +1234567890)
phone_number = '+917898808601'

# Specify the message to send
message = 'Hello this is whatsapp message'

# Send the message instantly
kit.sendwhatmsg_instantly(phone_number, message)