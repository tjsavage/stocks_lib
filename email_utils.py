import os
import smtplib
import string

from email import Encoders
from email.MIMEBase import MIMEBase
from email.MIMEMultipart import MIMEMultipart
from email.Utils import formatdate


def send_email(to = "stocks@taylorsavage.com",
		sender = "stocks@taylorsavage.com",
		subject = "Stocks Email",
		body = "",
		host = "smtp.gmail.com",
		attachment_paths = None):

	server = smtplib.SMTP(host, 587)
	server.ehlo()
	server.starttls()
	server.ehlo()
	server.login('stocks@taylorsavage.com', ')5F$1bB6A#72&09a4eF53^63@90#F4')
	if attachment_paths:
		msg = MIMEMultipart()
		msg["From"] = sender
		msg["To"] = to
		msg["Subject"] = subject
		msg["Date"] = formatdate(localtime=True)

		for attachment in attachment_paths:
			part = MIMEBase('application', "octet-stream")
			part.set_payload(open(attachment, "rb").read())
			Encoders.encode_base64(part)
			part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(attachment))
			msg.attach(part)

		try:
			failed = server.sendmail(sender, to, msg.as_string())
			server.close()
		except Exception, e:
			errorMsg = "Unable to send mail. Error: %s" % str(e)
			print errorMsg
	else:
		msg = string.join((
			"From: %s" % sender,
			"To: %s" % to,
			"Subject: %s" % subject,
			"",
			body
			), "\r\n")
		server.sendmail(sender, [to], msg)
		server.quit()

if __name__ == "__main__":
	to = raw_input("To: ")
	subject = raw_input("Subject: ")
	body = raw_input("Body: ")
	
	send_email(to=to, subject=subject, body=body)		
