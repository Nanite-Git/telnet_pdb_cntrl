from telnetlib import Telnet
with Telnet('localhost', 8888) as tn:
    while True:
        tn.write(b'step\n')
        input()