#!/usr/bin/env python3

import socket
import json
import sys

HOST = sys.argv[1]
PORT = int(sys.argv[2])


def command(cmd, timeout=3.0):
    cmd = len(cmd).to_bytes(2, byteorder='big') + bytes(cmd, 'ascii')

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.settimeout(timeout)
        s.sendall(cmd)

        r = bytes()
        while True:
            d = s.recv(4096)
            r += d

            if d[-2:] == b'\x00\x00':
                break

        msgs = []
        while len(r) > 0:
            l = int.from_bytes(r[0:2], byteorder='big')
            m = r[2:l + 1]

            if m:
                msgs.append(m.strip())

            r = r[l + 2:]

        return msgs


def parse_status(msgs):
    return {
        x[0].strip(): x[1].strip() for x in [
            m.decode('ascii').split(':', maxsplit=1) for m in msgs
        ]
    }


time_mult = {
    'Seconds': 1,
    'Minutes': 60,
    'Hours': 3600,
}


def parse_number(x):
    try:
        x = int(x)
    except:
        x = float(x)

    return x


r = {}
for k, v in parse_status(command('status')).items():
    t = v.split(' ')

    try:
        v = parse_number(t[0])
    except:
        pass

    if len(t) == 2 and t[1] in time_mult:
        v = v * time_mult[t[1]]

    r[k] = v

print(
    json.dumps(r, indent=2, sort_keys=True)
)
