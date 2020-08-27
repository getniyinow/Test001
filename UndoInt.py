
import getpass
import telnetlib

HOST = "192.168.157.21"
user = input("Enter your telnet username: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

tn.write(b"enable\n")
tn.write(b"cisco\n")
tn.write(b"config t\n")


mask=" 255.255.255.255"
for x in range (1,100):
    tn.write(b" no int loop " + str(x).encode('ascii') + b"\n")
#    tn.write(b"exit\n")
tn.write(b"exit\n")
tn.write(b"exit\n")


tn.write(b"show ip int bri | exc una\n")
tn.write(b"exit\n")



print(tn.read_all().decode('ascii'))


