import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

fromaddr = "setiyoh75@gmail.com"
toaddr = "rianiyoshania@gmail.com"
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Final Project Python"
 
body = "Selamat Pagi, berikut Tugas Python"
msg.attach(MIMEText(body, 'plain'))

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "yoshania")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()
