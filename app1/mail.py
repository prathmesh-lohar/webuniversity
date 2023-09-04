def sendmail(body):
    from email.message import EmailMessage
    import ssl
    import smtplib

    sender = 'debugnow.in@gmail.com'
    rec = "debugnow.in+contactus@gmail.com"
    pwd = 'matuhhcdubdepowc'

    body = body

    subject = "ContactUs"

    


    body = body

    em = EmailMessage()
    em['From'] = sender
    em['To'] = rec
    em['subject'] = subject
    em.set_content(body)

    contex = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com',465,context=contex) as smtp:
        smtp.login(sender,pwd)
        smtp.sendmail(sender,rec,em.as_string())

