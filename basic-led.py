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

def blinkSync(red, green, blue):
  red.blink(.5)
  green.blink(.5)
  blue.blink(.5)
    
def blink(red, green, blue):
  red.blink(.5)
  green.blink(1)
  blue.blink(1.5)
  
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
    
def handleLedUpdate(mode, modes, iteration, red, green, blue):
  currentPosition = mode % len(modes)
  currentMode = modes[currentPosition]
  if iteration <= 0:
    currentMode(red, green, blue)
  else:
    if currentMode == cycle and iteration % 200 == 0:
      currentMode(red, green, blue)
  return iteration + 1

def run():
  print('starting...')

  red = LED(25)
  green = LED(23)
  blue = LED(18)
  lb = Button(16)
  rb = Button(12)

  iteration = 0
  mode = 0
  modes = [off, on, blinkSync, blink, cycle]

  
  print('listening for input...')
  while True:

    iteration = handleLedUpdate(mode, modes, iteration, red, green, blue)
    
    if lb.is_pressed:
      print('updating mode')
      off(red, green, blue)
      mode = mode + 1
      iteration = 0
      print('mode set to ' + str(mode % len(modes)))
      sleep(.25)
      print('listening for input...')
      
    if rb.is_pressed:
      print('turning off lights')
      off(red, green, blue)
      mode = 0
      print('listening for input...')
      
run()