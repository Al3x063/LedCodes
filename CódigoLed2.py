from machine import Pin
from utime import sleep_ms as pausam
leda= Pin(2,Pin.OUT)
ledb= Pin(15,Pin.OUT)
ledc= Pin(16,Pin.OUT)
ledd= Pin(17,Pin.OUT)
lede= Pin(5,Pin.OUT)
ledf= Pin(18,Pin.OUT)
ledg= Pin(19,Pin.OUT)
ledh= Pin(3,Pin.OUT)
ledi= Pin(1,Pin.OUT)
ledj= Pin(22,Pin.OUT)

def print_led(a,b,c,d,e,f,g,h,i,j):
  leda.value(a)
  ledb.value(b)
  ledc.value(c)
  ledd.value(d)
  lede.value(e)
  ledf.value(f)
  ledg.value(g)
  ledh.value(h)
  ledi.value(i)
  ledj.value(j)
  pausam(50)
  
while False:
  print_led(0,0,0,0,0,0,0,0,0,1)
  print_led(0,0,0,0,0,0,0,0,1,0)
  print_led(0,0,0,0,0,0,0,1,0,0)
  print_led(0,0,0,0,0,0,1,0,0,0)
  print_led(0,0,0,0,0,1,0,0,0,0)
  print_led(0,0,0,0,1,0,0,0,0,0)
  print_led(0,0,0,1,0,0,0,0,0,0)
  print_led(0,0,1,0,0,0,0,0,0,0)
  print_led(0,1,0,0,0,0,0,0,0,0)
  print_led(1,0,0,0,0,0,0,0,0,0)


