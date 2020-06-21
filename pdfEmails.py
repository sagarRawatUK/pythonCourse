import smptlib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'Sender_name'
email['to'] = 'Receiver_eamil'
email['subject'] = 'Subject'

email.set_content('I am a Python Master')

with smtlib.SMTP(host='smtp.gmail.com',port=587) as smtp:
    smtp.shlo()
    smtp.starttls()
    smtp.login('Sender_email','password')
    smtp.send_message(email)
    print("All Done.")
    
