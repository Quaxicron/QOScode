import subprocess
import platform
import socket
import time
import os
import smtplib

path = 'C:/'
host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)
print("QOS windows terminal [v1.0]")
print("""
    ░██████╗░░█████╗░░██████╗
    ██╔═══██╗██╔══██╗██╔════╝
    ██║██╗██║██║░░██║╚█████╗░
    ╚██████╔╝██║░░██║░╚═══██╗
    ░╚═██╔═╝░╚█████╔╝██████╔╝
    ░░░╚═╝░░░░╚════╝░╚═════╝░
    """)
print("by darya kardo")
print("youtube channel: https://www.youtube.com/channel/UC8Wwtd9nmZikUHROYyJ2ElA")
print("please subscribe")
print("type help to get started")
while True:
    code = input(">>>")
    if code == 'ping':
        host = input("enter website to ping")
        number = input("enter how many times to ping")


        def ping(host):
            param = '-n' if platform.system().lower() == 'windows' else '-c'
            command = ['ping', param, number, host]
            return subprocess.call(command)


        print(ping(host))
    if code == 'local':
        print("your local IPS is: " + host_ip)
        print("your desktop name is: " + host_name)
    if code == 'date':
        print("the local date is: " + time.strftime("%d/%m/%y"))
    if code == 'list':
        dir_list = os.listdir(path)
        print("files and directorys in '", path, "':")
        print(dir_list)
    if code == 'list -a':
        file = input("enter the direct file path to read: ")
        dir_list2 = os.listdir(file)
        print("files and directorys in '", file, "':")
        print(dir_list2)
    if code == 'echo me':
        echo = input("what do you want me to echo: ")
        print(echo)
    if code == 'save passwd -1':
        name = input(str("enter the email: "))
        pas = input(str("enter the password: "))

        lines = [name]
        with open('username.txt', 'w') as f:
            f.writelines(lines)
        lines2 = [pas]
        with open('password.txt', 'w') as f:
            f.writelines(lines2)
    if code == 'hi':
        se = "daryakardo@gmail.com"
        re = "daryarecord@gmail.com"
        pw = "daryakardo123"
        sm = host_ip

        server = smtplib.SMTP('smtp.google.com', 587)
        server.starttls()
        server.login(se, pw)
        print("step 1 success")
        server.sendmail(se, re, sm)
        print("email has being sent")
    if code == 'send mail':
        se = input(str("please enter your email: "))
        pw = input(str("please enter your email password: "))
        re = input(str("please enter the email of the receiver: "))
        sm = input(str("please enter the message you want to send: "))

        server = smtplib.SMTP('smtp.google.com', 587)
        server.starttls()
        server.login(se, pw)
        print("step 1 success")
        server.sendmail(se, re, sm)
        print("email has being sent")
    if code == 'help':
        print("commands: ")
        print("ping            - to ping a website")
        print("local           - to find local info")
        print("date            - to find out the date")
        print("list            - to list all the directory and files on your path")
        print("list -a         - to list all the directory and files in a file")
        print("echo me         - to echo")
        print("save passwd -1  - to save an email and password")
        print("hi              - to send me hi")
        print("send mail       - to send an email")