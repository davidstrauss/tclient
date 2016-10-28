#!/usr/bin/python3

import socket
import re
import os

CRLF = "\r\n\r\n"

# export TABLE_ID=100
# export MARK=1
#
# echo "$TABLE_ID     tclient" | sudo tee -a /etc/iproute2/rt_tables
# sudo iptables -t mangle -A PREROUTING -d 127.0.0.1/24 -j MARK --set-mark $MARK
# sudo ip rule add fwmark $MARK lookup $TABLE_ID
# sudo ip route add local 127.0.0.1 dev lo table $TABLE_ID

def http_get():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.30)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    s.setsockopt(socket.SOL_IP, socket.IP_TRANSPARENT, 1)
    #s.bind(('10.0.0.1', 0))
    s.connect(('127.0.0.1', 80))
    s.send(b'GET / HTTP/1.0\r\n\r\n')
    data = (s.recv(1000000))
    print(data)
    s.shutdown(1)
    s.close()
    print('Received', repr(data))

if __name__ == "__main__":
    http_get()
