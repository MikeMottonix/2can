#from picamera import Picamera
import sys
import termios
import tty
import explorerhat
import time

inkey_buffer = 1 
#camera = Picamera()

print("Hallo Chauffeur,")
print(" ")
time.sleep(0.2)
print(" Steuere mit:")
print("   Q   W   E")
print("    A   S   D")
time.sleep(0.5)
print("Wenn du beenden willst drücke 1 und folge")
print("den Anweisungen.")
print("Los geht's:")
time.sleep(0.2)
print("Toturial: j/n?")
tutut = input()
if tutut == "j":
    print("Fahre mit W A S D im Kreis")
    print("Drücke 2")
print("Es gibt 2 Steuerungsmöglichkeiten:")
print("1. Freies einfaches Fahren mit Q W E A S D")
print("2. Oder programmiertes in cm ohne Steuerung")
steuer = input("1 oder 2: ")
steuer = int(steuer)
#if steuer == "2":
    #1sec == 11,5cm
#camera.start_preview()
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
    #ablauf = input()
    #action = input("Was nun?: ")
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
        print("Ende: drücke in 10sec StrgC.")
        time.sleep(10)
        print("Weiter geht's!")
    if key == "2":
        vorward()
        left()
        vorward()
        left()
        vorward()
        left()
        vorward()
        left()
        print("Jetzt du.")
        print("So das Programm hast du verstanden.")
