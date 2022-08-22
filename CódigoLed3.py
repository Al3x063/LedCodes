from machine import Pin
from utime import sleep, sleep_ms
led1= Pin(2,Pin.OUT)
led2= Pin(15,Pin.OUT)
led3= Pin(16,Pin.OUT)
led4= Pin(17,Pin.OUT)
led5= Pin(5,Pin.OUT)
led6= Pin(18,Pin.OUT)
led7= Pin(19,Pin.OUT)
led8= Pin(3,Pin.OUT)
led9= Pin(1,Pin.OUT)
led10= Pin(22,Pin.OUT)

leds = [led1,led2,led3,led4,led5,led6,led7,led8,led9,led10]

def ida():
  for i in leds:
      i.value(1)
      sleep_ms(50)
      i.value(0)
      sleep(0.05)
def regreso():
  for i in reversed(leds):
      i.value(1)
      sleep(0.05)
      i.value(0)
      sleep(0.05)
while True:
    ida()
    regreso()


