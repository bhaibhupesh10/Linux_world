import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(to_email, subject, body, smtp_server, smtp_port, login, password):
    msg = MIMEMultipart()
    msg['From'] = login
    msg['To'] = to_email
    msg['Subject'] = subject
    
    msg.attach(MIMEText(body, 'plain'))
    
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(login, password)
        text = msg.as_string()
        server.sendmail(login, to_email, text)
        server.quit()
        print(f"Email sent to {to_email}")
    except Exception as e:
        print(f"Failed to send email to {to_email}. Error: {str(e)}")

def send_bulk_emails(recipient_list, subject, body, smtp_server, smtp_port, login, password):
    for recipient in recipient_list:
        send_email(recipient, subject, body, smtp_server, smtp_port, login, password)

# Define email details
subject = "Hi, good morning everyone!!!"
body = "This is a test email sent in bulk."
smtp_server = "smtp.gmail.com"
smtp_port = 587
login = "aakarpawar7489@gmail.com"
password = "yhbc jymk iosz spjj" # Be cautious with hardcoding passwords

# List of recipient emails
recipient_list = [
    "gungunkhandelwal12@gmail.com",
    "bhupesh7750@gmail.com",
    "samirsinghjadon17@gmail.com",
    "anurag1342001@gmail.com"
]

# Send the emails
send_bulk_emails(recipient_list, subject, body, smtp_server, smtp_port, login, password)
