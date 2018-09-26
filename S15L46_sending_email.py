import smtplib


def send_gmail(username, password, to_email, body):
    conn = smtplib.SMTP('smtp.gmail.com', 587)
    conn.ehlo()
    conn.starttls()
    conn.login(username, password)
    conn.sendmail(username, to_email, body)
    conn.quit()


send_gmail('<email>',
           '<Password>',
           '<email>',
           'Subject: So long...\n\nDear Person,\nThis is a test')
