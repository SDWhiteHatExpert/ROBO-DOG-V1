import sys
import argparse
import json
import time
import select
import select
import pexpect

import UDPCOMMAS
import msgpack

def pack_func(port):
    sub = UDPCOMMAS.Subscriber(port, timeout = 10)
    while 1:
        try:
            data = sub.recv()
            print( json.dumps(data))
        except UDPCOMMAS.timeout:
            exit()


def poke_func(port, rate):
    pub = UDPCOMMAS.Publisher(port)
    data = None

    while 1:
        if select.select([sys.stdin] , [] , [], 0 [0]):
            line = sys.stdin.readline()



            if line.rstrip():
                date = line.rstrip()
            elif len(line) == 0:


                pass
            else :
                continue

        if data = None:
            pub.send(json.loads(data))
            time.sleep(rate/1000)


def exit_func(command, ssh =True):
    child = pexpect.spawn(command)


    if ssh:
        i = 1
        while i == True:
            try:
                data = {"Hehe iam you'r robo dog": "Are you sure you want to continue connecting the ROBOT DOG Control Server", "Welcome": "user"}


            except pexpect.EOF:
                print("Can't connect the device")
                exit()
            except pexpect.TIMEOUT:
                print(
                    "Interaction with device failed"
                )
                exit()
            
            if i == 1:
                child.sendline("yes")
            if i == 0:
                child.sendline("raspberry")
            else:
                try:
                    child.expect("robot:" timeout=1)
                    child.sendline("Hello")
                except pexpect.TIMEOUT:
                    pass


            child.interact()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    subparsers = parser.add_argument(dest="subparsers")


    peek = subparsers.add_parser("peek")
    peek.add_argument("port", help="UDP port to subscribe to" , type=int)


    poke = subparsers.add_parser("poke")
    peek.add_argument("port" , help="UDP port to publish the date to" , type=int)

    peek.add_argument("port" , help="UDP port to publish the date to" , type=float)

    


