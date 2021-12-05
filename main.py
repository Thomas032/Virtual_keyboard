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


class Led():
    def __init__(self):
        self.led = digitalio.DigitalInOut(board.GP22)
        self.led.direction = digitalio.Direction.OUTPUT
    
    def on_set(self, reps, delay):
        for i in range(reps):
            if i%2 == 0:
                self.led.value = True
            else:
                self.led.value = False
            if delay:
                time.sleep(delay)
            else:
                pass
    def ON(self):
        self.led.value = True
    def OFF(self):
        self.led.value = False
        
        
class K_keyboard():
    def __init__(self):
        self.kbd = Keyboard(usb_hid.devices)
        self.layout = KeyboardLayoutUS(self.kbd)
        
    def caps(self,state): 
        if state == 1:
            self.kbd.send(Keycode.CAPS_LOCK)
        if state == 0:
            self.kbd.send(Keycode.CAPS_LOCK)
        
    def num(self,state):
        
        if state == 1:
            self.kbd.send(Keycode.KEYPAD_NUMLOCK)
        if state == 0:
            self.kbd.send(Keycode.KEYPAD_NUMLOCK)
            
    def page(self, state):
        if state == 1:
            self.kbd.send(Keycode.SCROLL_LOCK)
        if state == 0:
            self.kbd.send(Keycode.SCROLL_LOCK)  
        
    def swich_kbd(self):
        time.sleep(1)
        reps = 0
        if reps == 0:
            self.kbd.send(Keycode.GUI, Keycode.SPACE)
            reps = 1
        
    def roll(self): 
        time.sleep(1)
        self.kbd.send(Keycode.GUI, Keycode.R)
        urls = ["https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstleyVEVO",\
                "https://www.youtube.com/watch?v=trDCzyyXGjw",\
                "https://www.youtube.com/watch?v=C0C3NK55tI8&t=17s"]
        url = random.choice(urls)
        time.sleep(0.1)
        self.layout.write(url)
        self.kbd.send(Keycode.ENTER)
        
    def sleep(self):
        self.swich_kbd()
        self.kbd.send(Keycode.GUI, Keycode.R)
        dobrou = "https://www.youtube.com/watch?v=HrU22eV4gxM&ab_channel=R%C3%A1dioKrab&t=24s"
        time.sleep(0.1)
        self.layout.write(dobrou)
        self.kbd.send(Keycode.ENTER)
    def shut_down(self):
        self.kbd.send(Keycode.ALT, Keycode.F4)
        time.sleep(.1)
        self.kbd.send(Keycode.ALT, Keycode.F4)
        time.sleep(.1)
        self.kbd.send(Keycode.ENTER)
    def initialised(self, rolls):
        if rolls:
            for i in range(rolls):
                self.num(1)
                self.page(1)
                time.sleep(.5)
                self.num(0)
                self.page(0)
                self.caps(1)
                time.sleep(.5)
                self.caps(0)
                
    def change_monitor(self, monitor):
        if monitor == "01":
            for i in range(4):
                self.kbd.send(Keycode.GUI, Keycode.P)
            self.kbd.send(Keycode.Enter)
        if monitor == "11":
            for i in range(2):
                self.kbd.send(Keycode.GUI, Keycode.P)
            time.sleep(.01)
            self.kbd.send(Keycode.Enter)
            
        
        if monitor == "00":
            for i in range(3):
                self.kbd.send(Keycode.GUI, Keycode.P)
            time.sleep(.01)
            self.kbd.send(Keycode.Enter)
        if monitor == "10":
            for i in range(4):
                self.kbd.send(Keycode.GUI, Keycode.P)
            time.sleep(.01)
            self.kbd.send(Keycode.Enter)
           
class M_mouse():
    def __init__(self):
        self.m = Mouse(usb_hid.devices)
        
    def mouse(self):
        while True:
            delay = random.uniform(5, 30)
            pos = random.randint(1,150)
            self.m.move(x=-pos)
            time.sleep(delay)
            self.m.move(x=pos)
            time.sleep(delay)
            if pos >= 75:
                self.m.click(Mouse.LEFT_BUTTON)
    def keep_mouse(self, pos_x, pos_y):
        while True:
            self.m.move(pos_x, pos_y, 0)
            self.m.press(Mouse.LEFT_BUTTON)
            self.m.press(Mouse.LEFT_BUTTON)

class C_consumer():
    def __init__(self):
        self.consumer = ConsumerControl(usb_hid.devices)
        
    def volume(self, level, quantity):
        for i in range(quantity):
            if level == 1:
                self.consumer.send(ConsumerControlCode.VOLUME_INCREMENT)
            if level == 0:
                self.consumer.send(ConsumerControlCode.VOLUME_DECREMENT)

        
    def eject(self, loops):
        self.consumer.send(ConsumerControlCode.EJECT)

    
class Basics():       
    def block_mose_move(self):
        global khundalini, mys
        time.sleep(0.3)
        khundalini.change_monitor("01") 
        mys.keep_mouse(200,200)
    def classic(self):
        global played, khundalini, m
        if played == 0:
            time.sleep(5)
            khundalini.swich_kbd()
            time.sleep(3)
            khundalini.roll()
            
        else:
            time.sleep(3)
            khundalini.roll()
        played +=1
    def end():
        global khundalini
        time.sleep(.5)
        khundalini.sleep()
        time.sleep(4)
        khundalini.shut_down()
         
            
""" GLOBAL VARIABLES """
played = 0
khundalini = K_keyboard()
mys = M_mouse()
consumer = C_consumer()

basics = Basics()

btn1 = digitalio.DigitalInOut(board.GP20)
btn2 = digitalio.DigitalInOut(board.GP21)
btn1.direction = digitalio.Direction.INPUT
btn2.direction = digitalio.Direction.INPUT
led = Led()



""" !-GLOBAL VARIABLES-!"""    


"""FUNC_CALL FIELD"""
khundalini.initialised(3)
while True:
    if btn1.value == True:
        basics.classic()
    if btn2.value == True:
        led.on_set(50, 0.05)


""" !-END OF FUNC_CALL FIELD-! """


