import requests
import cv2
import time
import RPi.GPIO as GPIO
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008


if __name__ == '__main__':
        # ------------------------Set up for LED and Potentiometer---------------------------
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
        # -------------------------Record and send image from RPi to Server ----------------------
        # Start recording
        cam = cv2.VideoCapture(0)
    
        # Caputure the imgage
        ret, image = cam.read()
        cam.release()
    
        # Turn the image into jpg file
        _, buffer = cv2.imencode('.jpg', image)
    
        # Send the image via HTTP POST
        headers = {"Content-Type": "image/jpeg"}  # Indicate JPEG format
        response = requests.post(url, data=buffer.tobytes(), headers=headers)
        # ----------------------Process response from server---------------------------
        # Parse the JSON file
        # Message1 : image upload confirmation message
        # Message2 : command to turn on or off light, ouput by ML model
        message = response.json()
    
        # Check the response status code
        if response.status_code == 200:
            print("Image uploaded successfully")
            print(message["message1"])
            # If message2 = True turn on light, else turn off
            if (mcp.read_adc(0) > 530) and (flag == False) and message["message2"]:
                # If potentiometer is turned to upper half, turn on Red LED
                GPIO.output(led, GPIO.LOW)
                led = [11]
                flag = True
                GPIO.output(led, GPIO.HIGH)
                print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
                print("Turning on Red LED")
                print("Potentiometer Channel 0: ", mcp.read_adc(0))
                print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
            elif (mcp.read_adc(0) <= 500) and (flag == True) and message["message2"]: 
                # If potentiometer is turned to lower half, turn on Yellow LED
                GPIO.output(led, GPIO.LOW)
                led = [15]
                flag = False
                GPIO.output(led, GPIO.HIGH)
                print("-------------------------------------------")
                print("Turning on Yellow LED")
                print("Potentiometer Channel 0: ", mcp.read_adc(0))
                print("-------------------------------------------")
            elif not message["message2"]:
                GPIO.output(led, GPIO.LOW)
        else:
            print("Error uploading image:", response.status_code)

        
