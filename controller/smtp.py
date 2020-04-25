import smtplib
# content="test"

def mail_verification_code():
	mail = smtplib.SMTP('smtp.gmail.com', 587)
	sender = 'quizmovie7@gmail.com'
	receivers = ['risal.irish@gmail.com']
	mail.starttls()
	mail.login("quizmovie7@gmail.com","pdrgkgxuliyxlkqm")
	message = """From: quizmovie7 <from@fromdomain.com>
	To: To Person <to@todomain.com>
	Subject: user verification

	This is a test e-mail message.
	"""

	try:
	   # smtpObj = smtplib.SMTP('localhost')
	   mail.sendmail(sender, receivers, message)         
	   print ("Successfully sent email")
	except Exception:

		# print(e)
		return "Error: unable to send email"


# mail_verification_code()