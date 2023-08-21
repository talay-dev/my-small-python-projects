import smtplib


myemail = 'example@example.com'
##Write here mail access password
mypassword = ''
takermail = 'example2@example.com'

def conntomail(mail = myemail, to_mail = takermail, passcode = mypassword):
    connection = smtplib.SMTP('smtp.gmail.com',port=587)

    print('connected')
    connection.starttls()
    connection.login(user=mail, password=passcode)
    connection.sendmail(from_addr=mail,to_addrs=to_mail,msg="Subject:ISS\n\nHeyy!! ISS near to you look at sky")

    print('okay')
    connection.close()



