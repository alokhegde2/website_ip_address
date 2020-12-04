# get any website ip address using Python

import socket as s

host = input("Enter the Website name / host name :")
print(f'IP of {host} is {s.gethostbyname(host)}')