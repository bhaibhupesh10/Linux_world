import pywhatkit as kit

def setTime():
    hour = int(input("Enter hour"))
    minute = int(input("Enter minute"))
    kit.sendwhatmsg("+917489356891", "Hi this is Bhupesh", hour, minute)


def sendInstant():
    # Specify the recipient's phone number (including country code, e.g., +1234567890)
    phone_number = '+917489356891'

    # Specify the message to send
    message = 'Hello! How are you'

    # Send the message instantly
    kit.sendwhatmsg_instantly(phone_number, message)

def main():
    print("Do you want to \n1. Set time \n2. Instant")
    x1 = int(input("enter choice: "))
    if x1==1:
        setTime()
    elif x1==2:
        sendInstant()
    else:
        print("invalid input")

if __name__ == "__main__":
    main()