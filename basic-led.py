from gpiozero import LED, Button
from time import sleep

def off(red, green, blue):
  red.off()
  green.off()
  blue.off()

def on(red, green, blue):
  red.on()
  green.on()
  blue.on()

def blink(red, green, blue):
  red.blink()
  green.blink()
  blue.blink()
  
def cycle(red, green, blue):
  if red.is_lit:
    red.off()
    green.on()
  elif green.is_lit:
    green.off()
    blue.on()
  elif blue.is_lit:
    blue.off()
    red.on()
  else:
    red.on()
    green.off()
    blue.off()

def run():
  print('starting...')

  red = LED(25)
  green = LED(23)
  blue = LED(18)
  lb = Button(16)
  rb = Button(12)

  mode = 0
  modes = [off, on, blink, cycle]
  
  print('listening for input...')
  while True:
    modes[mode % len(modes)](red, green, blue)
    if lb.is_pressed:
      print('updating mode')
      off(red, green, blue)
      mode = mode + 1
      print('mode set to ' + str(mode % len(modes)))
      sleep(.25)
      print('listening for input...')
      
    if rb.is_pressed:
      print('turning off lights')
      off(red, green, blue)
      mode = 0
      print('listening for input...')
      
run()