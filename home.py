import time
import os
import socket
import psutil
import pynotifier

has_battery = psutil.sensors_battery() is not None
battery = psutil.sensors_battery()
login_pass = open('user/password.txt')
login_name = open('user/username.txt')
l_p = login_pass.read()
l_n = login_name.read()
print("""
░██████╗░░█████╗░░██████╗
██╔═══██╗██╔══██╗██╔════╝
██║██╗██║██║░░██║╚█████╗░
╚██████╔╝██║░░██║░╚═══██╗
░╚═██╔═╝░╚█████╔╝██████╔╝
░░░╚═╝░░░░╚════╝░╚═════╝░
""")
print("Welcome " + l_n)
print("The Date Is: " + time.strftime("%d/%m/%y"))
print("Running On Battery: ")
print(has_battery)
if has_battery == "True":
    print("Battery Level Is: ")
    print(battery.percent)
    pynotifier.Notification("Battery Percentage: ", str(battery.percent) + "%Percent Remaining", duration=20).send()
print("""
[1] To Open Google
[2] To Open Text Editor
[3] To Open File Explorer
[4] To Configure And Open BIOS
[5] To Close OS Safely
[6] To Open Terminal
[7] To Open Sendmail
""")
select = input("[?]: ")

if select == '1':
    os.startfile('brows.py')

if select == '2':
    os.startfile('edit.py')

if select == '3':
    os.startfile('file.py')

if select == '4':
    b_login = input(str("Please Enter The Password To " + l_n + " To Open BIOS: "))
    if b_login == l_p:
        print("Opening BIOS")
        host_name = socket.gethostname()
        host_ip = socket.gethostbyname(host_name)
        print("[1] USERNAME: " + l_n)
        print("[2] PASSWORD: " + l_p)
        print("HOSTNAME: ", host_name)
        print("LOCAL IP: " + host_ip)
        edit_b = input("Enter [?] TO Change Settings: ")
        if edit_b == '1':
            edit_n = input("Enter Your New Username: ")
            with open('user/username.txt', 'w') as f:
                f.writelines(edit_n)
            print("Username Changed TO " + edit_n)
            input("Press Enter To Close Window: ")

        if edit_b == '2':
            edit_p = input("Enter New Password: ")
            with open('user/username.txt', 'w') as f:
                f.writelines(edit_p)
            print("Password Changed TO " + edit_p)
            input("Press Enter To Close Window: ")

    else:
        print("Wrong Password To" + l_n)

if select == '6':
    os.startfile(qosterminal.py)

if select == '7':
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