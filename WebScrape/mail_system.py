import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase


def email_send(filename) :
    file_r = open(filename,'rb')
    part = MIMEBase('application','octet-stream') 
    part.set_payload((file_r).read())
    encoders.encode_base64(part) #encode the attachment by reading the byte scheme
    part.add_header('Content-Disposition','attachment; filename=' + filename)
    server = smtplib.SMTP('smtp.gmail.com',587) #connects to the host
    server.starttls() #secure the server
    server.login('abhilashsaravana0@gmail.com','hgjzxtselolioslm') #logs in to the account
    from_add = 'abhilashsaravana0@gmail.com'
    to_add = 'abhilashsaravana@yahoo.com'
    subject = 'Stock information'
    message = MIMEMultipart()
    message['From'] = from_add
    message['To'] = to_add
    message['Subject'] = subject
    message.attach(part) #attach the file

    msg = "This email contains the csv file with stock information of google, Tesla and Eli Lilly"
    message.attach(MIMEText(msg,'plain'))
    text = message.as_string()
    server.sendmail(from_add,to_add,text)

    server.quit()