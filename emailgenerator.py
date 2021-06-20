import smtplib

class Email_send:

    def __init__(self, EMAIL_ADDRESS, PASSWORD):

        self.email = EMAIL_ADDRESS
        self.password = PASSWORD 
        self.server = smtplib.SMTP('smtp.gmail.com:587')
        self.server.ehlo()
        self.server.starttls()
        self.server.login(self.email, self.password)

    def send_email(self, subject, msg, listofaddress):
        try:
            message= 'Subject:{}\n\n{}'.format(subject,msg)
            self.server.sendmail(EMAIL_ADDRESS,listofaddress,message)
            print("Success:Email Sent!")
        except:
            print("Email failed to send")


EMAIL_ADDRESS="snp.project234@gmail.com"
PASSWORD="snpproject@123"

sendl = Email_send(EMAIL_ADDRESS, PASSWORD)

print("Enter the subject")
subject=input()

print("Enter the message to be sent")
msg=input()

print("Enter the recipient adressess")
listofaddress=list(map(str,input().split()))

sendl.send_email(subject, msg, listofaddress)
