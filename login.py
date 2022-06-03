import socket
import time
import os
import qosterminal

print("[v1.0]")
print("""
░██████╗░░█████╗░░██████╗
██╔═══██╗██╔══██╗██╔════╝
██║██╗██║██║░░██║╚█████╗░
╚██████╔╝██║░░██║░╚═══██╗
░╚═██╔═╝░╚█████╔╝██████╔╝
░░░╚═╝░░░░╚════╝░╚═════╝░
""")
print("The Date Is: " + time.strftime("%d/%m/%y"))
print("""
[1] Continue With Setup
[2] I've Already Done Setup
[3] Open Terminal
[4] Open BIOS
""")
setup = input("[?]: ")
if setup == '1':
    name = input(str("Please Enter Your User Name To Be Displayed: "))
    pas = input(str("Please Enter Your Password To Login: "))

    with open('user/username.txt', 'w') as f:
        f.writelines(name)

    with open('user/password.txt', 'w') as f:
        f.writelines(pas)
    print("Setup Complete!!!")
    input("Press Enter To Close Window: ")
    l_n = name
    l_p = pas

if setup == '2':
    login_pass = open('user/password.txt')
    login_name = open('user/username.txt')
    l_p = login_pass.read()
    l_n = login_name.read()

while True:
    login = input(str("Please Enter The Password To " + l_n + ": "))
    if login == l_p:
        os.startfile('home.py')
        break
    else:
        print("Wrong Password!")

if setup == '3':
    os.startfile(qosterminal.py)

if setup == '4':
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