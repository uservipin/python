# Python code to illustrate Sending mail from
# your Gmail account
import smtplib

Mail_id="kumar.vipin1v00@gmail.com"
password= "01091996"
Sender_Mail_Id="vipin@strolar.com"
# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)
# start TLS for security
s.starttls()
# Authentication
s.login(Mail_id, password)
# message to be sent
message = "Dear Sir," \ 
          "this is vipin kumar from strolar mountings " \ 
          "hello , i am testing this mail for sending mail " \
          "to my mail id " \
          "" \
          "" \
          "" \
          "" \
          "" \
          "Thanks and regards " \
          "VIPIN KUMAR" \
          "7500574058" \
          "vipin@strolar.com"
# sending the mail
s.sendmail(Mail_id, Sender_Mail_Id, message)
# terminating the session
s.quit()
