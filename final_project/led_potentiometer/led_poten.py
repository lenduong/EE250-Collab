import time
import RPi.GPIO as GPIO
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008

#using physical pin 11 to blink Red LED, 15 to blink Yellow LED
GPIO.setmode(GPIO.BOARD)
red_led = [11]
yellow_led = [15]
GPIO.setup(red_led, GPIO.OUT)
GPIO.setup(yellow_led, GPIO.OUT)

# Hardware SPI configuration:
SPI_PORT   = 0
SPI_DEVICE = 0
mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))

flag = True # True = Red is on, False = Yellow is on
led = [11]

while True:  
  
  # GPIO.output(red_led, GPIO.HIGH)
  # print("turning on Red LED")
  # print("Potentiometer Channel 0: ", mcp.read_adc(0))
  # print("Potentiometer Channel 1: ", mcp.read_adc(1))
  # time.sleep(1)
  # GPIO.output(red_led, GPIO.LOW)
  # GPIO.output(yellow_led, GPIO.HIGH)
  # print("turning on Yellow LED")
  # print("Potentiometer Channel 0: ", mcp.read_adc(0))
  # print("Potentiometer Channel 1: ", mcp.read_adc(1))
  # time.sleep(1)
  # GPIO.output(yellow_led, GPIO.LOW)

  
  if (mcp.read_adc(0) > 530) and (flag == False) :
    # If potentiometer is turned to upper half, turn on Red LED
    GPIO.output(led, GPIO.LOW)
    led = [11]
    flag = True
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    print("Turning on Red LED")
    print("Potentiometer Channel 0: ", mcp.read_adc(0))
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
  elif (mcp.read_adc(0) <= 500) and (flag == True): 
    # If potentiometer is turned to lower half, turn on Yellow LED
    GPIO.output(led, GPIO.LOW)
    led = [15]
    flag = False
    print("-------------------------------------------")
    print("Turning on Yellow LED")
    print("Potentiometer Channel 0: ", mcp.read_adc(0))
    print("-------------------------------------------")
    
  GPIO.output(led, GPIO.HIGH)

  
  # #Following commands control the state of the output
  # for i in range (0,5):
  #   GPIO.output(chan_list, GPIO.HIGH)
  #   time.sleep(0.5)
  #   GPIO.output(chan_list, GPIO.LOW)
  #   time.sleep(0.5)
  # for i in range (0,50):
  #   time.sleep(0.1)
  #   light_reading = mcp.read_adc(0)
  #   if light_reading >lux_treshold:
  #     print("(BRIGHT) Light sensor reading: ", mcp.read_adc(0))
  #   else :
  #     print("(DARK) Light sensor reading: ", mcp.read_adc(0))

  # for i in range (0,4):
  #   GPIO.output(chan_list, GPIO.HIGH)
  #   time.sleep(0.2)
  #   GPIO.output(chan_list, GPIO.LOW)
  #   time.sleep(0.2)

  # for i in range (0,50):
  #   time.sleep(0.1)
  #   sound_reading = mcp.read_adc(1)
  #   if sound_reading >sound_treshold:
  #     GPIO.output(chan_list, GPIO.HIGH)
  #   else :
  #     GPIO.output(chan_list, GPIO.LOW)

  # # get reading from adc 
  # print("Light sensor reading: ", mcp.read_adc(0))
  # print("Sound sensor reading: ", mcp.read_adc(1))
