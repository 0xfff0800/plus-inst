from __future__ import absolute_import
from __future__ import print_function
import datetime
import requests
import smtplib
import time
import ssl
import bs4


A = """
<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>
<          plus inst                    >
< snapchat.com/add/flaah999             >
< instagram.com/0xfff0800               >
< T.me/Xfff0800                         >
<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>

"""
print ("")
print(A)


user = input('Enter the account name : ')
go = input('Your e-mail : ')
gu = input('Your password e-mail : ')
lo = input('Send an alert to this email : ')
not_available = True
target_username = ''+user+''
target_site = 'https://instagram.com/' + target_username + "/"
email_from = ''+go+''
email_from_password = ''+gu+''
email_to = ''+lo+''
message_to_url = 'Tell me, I love you, a falah'
message_to_send = 'Now the username is available for you go to Instagram !\n' + target_site + '\n' + message_to_url + '\n'


def start_ig_loop():
    global not_available

    while not_available:
        try:
            session = requests.get(target_site)
            document = bs4.BeautifulSoup(session.content, 'html.parser')

            page_title = document.title.text

            if "Not Found" in page_title:
                send_email()
                not_available = False
                exit(1)
            else:
                print(datetime.datetime.now().strftime('[%m-%d-%y, %I:%M:%S %p]') + ' Not yet available')
                time.sleep(1)
        except Exception as e:
            print(e)


def send_email():
    smtp_server = 'smtp.gmail.com'
    port = 465


    context = ssl.create_default_context()



    try:
        server = smtplib.SMTP_SSL(smtp_server, port, context=context)
        server.ehlo()
        server.login(email_from, email_from_password)
        server.sendmail(email_from, email_to, message_to_send)
    except Exception as e:

        print(e)


start_ig_loop()
