import time
import adafruit_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.mouse import Mouse
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode
import usb_hid
import board
import digitalio
import random

"""
DEBUGING LED (board implemented)
led = digitalio.DigitalInOut(board.GP25)
led.direction = digitalio.Direction.OUTPUT
"""

def caps(state): #turn on/off capslock
    global kbd
    if state == 1:
        kbd.send(Keycode.CAPS_LOCK)
    if state == 0:
        kbd.send(Keycode.CAPS_LOCK)
    
def num(state):
    global kbd
    if state == 1:
        kbd.send(Keycode.KEYPAD_NUMLOCK)
    if state == 0:
        kbd.send(Keycode.KEYPAD_NUMLOCK)
def page(state):
    global kbd
    if state == 1:
        kbd.send(Keycode.SCROLL_LOCK)
    if state == 0:
        kbd.send(Keycode.SCROLL_LOCK)
            
#IMPORTANT SECION !!
kbd = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(kbd)
consumer = ConsumerControl(usb_hid.devices)
m = Mouse(usb_hid.devices)
#END OF IMPORTANT SECTION !!

def swich_kbd(): #problemwith running twice needs three sys languages for kbd
    global kbd
    time.sleep(1)
    reps = 0
    if reps == 0:
        kbd.send(Keycode.GUI, Keycode.SPACE)
        reps = 1
    
def roll(): #play video needs us keyboard
    global kbd, layout
    time.sleep(1)
    kbd.press(Keycode.GUI, Keycode.R)
    kbd.release(Keycode.GUI, Keycode.R)
    urls = ["https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstleyVEVO", "https://www.youtube.com/watch?v=trDCzyyXGjw", "https://www.youtube.com/watch?v=C0C3NK55tI8&t=17s"]
    url = random.choice(urls)
    time.sleep(1)
    layout.write(url)
    kbd.send(Keycode.ENTER)
def sleep():
    global kbd, layout
    kbd.press(Keycode.GUI, Keycode.R)
    kbd.release(Keycode.GUI, Keycode.R)
    dobrou = "https://www.youtube.com/watch?v=HrU22eV4gxM&ab_channel=R%C3%A1dioKrab&t=24s"
    time.sleep(1)
    layout.write(dobrou)
    kbd.send(Keycode.ENTER)
    
def shut_down():
    global kbd
    time.sleep(2)
    kbd.send(Keycode.ALT, Keycode.F4)
    time.sleep(.2)
    kbd.send(Keycode.ALT, Keycode.F4)
    kbd.send(Keycode.ALT, Keycode.F4)
    kbd.send(Keycode.ENTER)
        
def initialised(rolls):
    
    if rolls:
        for i in range(rolls):
            num(1)
            page(1)
            time.sleep(.5)
            num(0)
            page(0)
            caps(1)
            time.sleep(.5)
            caps(0)

def mouse():
    global m
    
    while True:
        delay = random.uniform(5, 45)
        pos = random.randint(1,150)
        m.move(x=-pos)
        time.sleep(dela)
        m.move(x=pos)
        time.sleep(delay)
        if delay >= 30:
            m.click(Mouse.LEFT_BUTTON)
            
def volume():
    consumer.press(ConsumerControlCode.VOLUME_INCREMENT)
    time.sleep(0.5)
    consumer.release()

initialised(3)
#time.sleep(600) 600 seconds are used withthe whole show
time.sleep(10)
#swich_kbd()
#time.sleep(.3)
#roll()
mouse()
#time.sleep(300)
#sleep()


    



