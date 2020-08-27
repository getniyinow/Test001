import getpass
import telnetlib

HOST = "192.168.157.21"
user = input("Enter your telnet username: ")
password = getpass.getpass()
## let see if this works.###
tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

tn.write(b"enable\n")
tn.write(b"cisco\n")
tn.write(b"config t\n")
tn.write(b"int loop1 \n")
tn.write(b"ip add 10.10.10.1 255.255.255.255\n")
tn.write(b"exit\n")
tn.write(b"int loop2 \n")
tn.write(b"ip add 10.10.10.2 255.255.255.255\n")
tn.write(b"int loop3 \n")
tn.write(b"ip add 10.10.10.3 255.255.255.255\n")
tn.write(b"exit\n")
tn.write(b"exit\n")
tn.write(b"copy run start\n")
tn.write(b"\n")
tn.write(b"\n")
tn.write(b"exit\n")


tn.write(b"show ip int bri | exc una\n")
tn.write(b"exit\n")



print(tn.read_all().decode('ascii'))


