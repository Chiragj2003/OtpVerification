from random import randint, random 
import smtplib
from email.message import EmailMessage
import ssl

password ="kqewttyiqrakmnyy"

def otp_generator():
    # otp = random.randint(100000,1000000)
    # a=str(otp)
    a=str(5555)
    return a

    
def otp_checker(otp):
    user =input("enter the otp ") 
    if user == otp:
        print("access granted ")
    else :
        print("access denied ")



password ="kqewttyiqrakmnyy"

def sendemail ():
    email_sender="chiragj2019@gmail.com"
    a =input("enter the receiver mail = ")
    email_receiver = a
    password="kqewttyiqrakmnyy"

    textfile = otp_generator()
    body = f"thanks for using our service the otp is == {textfile}"
    em= EmailMessage()
    
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = 'The login OTP '
    em.set_content(body)
    
    content = ssl.create_default_context()
    
    with smtplib.SMTP_SSL('smtp.gmail.com',465,context=content) as smtp :
        smtp.login(email_sender,password)
        smtp.sendmail(email_sender,email_receiver,em.as_string())
        
    otp_checker(textfile)


sendemail()
