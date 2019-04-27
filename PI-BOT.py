#PI-BOT V2.3
#By https://github.com/MikeMottonix
#DO NOT COPY THIS AND SAY ITS YOURS

import sys
import termios
import tty
import explorerhat
import time

inkey_buffer = 1 


print("Hello Driver,")
print("Quit With 1 then STRG + C")
print(" ")
time.sleep(0.2)
print(" Controll With:")
print("   Q   W   E")
print("    A   S   D")

def inkey():
    fd=sys.stdin.fileno()
    remember_attributes=termios.tcgetattr(fd)
    tty.setraw(sys.stdin.fileno())
    charakter=sys.stdin.read(inkey_buffer)
    termios.tcsetattr(fd,termios.TCSADRAIN, remember_attributes)
    return charakter

def vorward():
    explorerhat.motor.one.forward()
    explorerhat.motor.two.forward()
    time.sleep(0.01)
    explorerhat.motor.one.stop()
    explorerhat.motor.two.stop()

def backward():
    explorerhat.motor.one.backward()
    explorerhat.motor.two.backward()
    time.sleep(0.01)
    explorerhat.motor.one.stop()
    explorerhat.motor.two.stop()

def right():
    explorerhat.motor.one.forward()
    explorerhat.motor.two.backward()
    time.sleep(0.01)
    explorerhat.motor.one.stop()
    explorerhat.motor.two.stop()

def left():
    explorerhat.motor.one.backward()
    explorerhat.motor.two.forward()
    time.sleep(0.01)
    explorerhat.motor.one.stop()
    explorerhat.motor.two.stop()


while True:
    key = inkey()
    if key == "w":
        vorward()
    if key == "s":
        backward()
    if key == "d":
        left()
    if key == "a":
        right()
    if key == "q":
        right()
        right()
        vorward()
        right()
    if key == "e":
        left()
        left()
        vorward()
        left()
    if key == "1":
        print("PRESS STRG + C to quit.")
        time.sleep(10)
