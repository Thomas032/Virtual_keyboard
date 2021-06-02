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
            
""" GLOBAL VARIABLES """
kbd = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(kbd)
consumer = ConsumerControl(usb_hid.devices)
m = Mouse(usb_hid.devices)
""" !-GLOBAL VARIABLES-!"""

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
    time.sleep(.2)
    kbd.send(Keycode.ALT, Keycode.F4)
    time.sleep(.2)
    kbd.send(Keycode.ALT, Keycode.F4)
    time.sleep(.2)
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
        delay = random.uniform(5, 30)
        pos = random.randint(1,150)
        m.move(x=-pos)
        time.sleep(delay)
        m.move(x=pos)
        time.sleep(delay)
        if pos >= 75:
            m.click(Mouse.LEFT_BUTTON)
            
def volume(level, quantity):
    global consumer
    for i in range(quantity):
        if level == 1:
            consumer.send(ConsumerControlCode.VOLUME_INCREMENT)
        if level == 0:
            consumer.send(ConsumerControlCode.VOLUME_DECREMENT)
    
    
    

def keep_mouse(pos_x, pos_y):
    global m
    while True:
        m.move(pos_x, pos_y, 0)
        m.press(Mouse.LEFT_BUTTON)
        m.press(Mouse.LEFT_BUTTON)
def change_monitor(monitor):
    global kbd
    """
    EXPLANATION OF VAR MONITOR:
        01 = > you only see the second monitor (in our case turned off projector)
        11 = > you see both screens at once (monitor and projector are duplicating)
        00 = > you see both but they are not duplicating it is extended
        10 = > you see only the pc screen and the projector is turned off (this only applies to our pc !) /on other computers it is in reverse (01 and 10)
    """
    if monitor == "01":
        kbd.send(Keycode.GUI, Keycode.P)
        kbd.send(Keycode.Enter)
    if monitor == "11":
        for i in range(2):
            kbd.send(Keycode.GUI, Keycode.P)
        time.sleep(.01)
        kbd.send(Keycode.Enter)
        
    
    if monitor == "00":
        for i in range(3):
            kbd.send(Keycode.GUI, Keycode.P)
        time.sleep(.01)
        kbd.send(Keycode.Enter)
    if monitor == "10":
        for i in range(4):
            kbd.send(Keycode.GUI, Keycode.P)
        time.sleep(.01)
        kbd.send(Keycode.Enter)
            
        
        
def block():
    time.sleep(0.3)
    change_monitor("01") MUST CHANGE!!
    volume(0, 100)
    keep_mouse(800,800)
     
def basic():
    time.sleep(10)
    swich_kbd()
    time.sleep(5)
    roll()
    
def end():
    time.sleep(5)
    sleep()
    time.sleep(4)
    shut_down()
def nenasravacka():
    mouse()
"""FUNC_CALL FIELD"""

initialised(3) #blink the leds for 3 times optional
block() #block the user from signing out
#nenasravacka() #just moving the mouse
#basic()
#end()

""" !-END OF FUNC_CALL FIELD-! """
  

# 
#                                          A
#             ___                         / \
#          .="   "=._.---.               /   \              ____________
#        ."         c ' Y'`p            /     \            /)  -
#       /     \     `\  w_/            :~~~~~~~:          / )-   .   -
#       |      )  /     /              |   1.E |         <  )      -- 
# ______|     /__-\ \_=.\              |       |          \ )  -      -
#(XXXXX/'`------)))`=-'"`'"___________/__/__\___\___ _ _ _ \)___________
# ~~~~~