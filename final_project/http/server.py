from flask import Flask
from flask import jsonify
from flask import request
from PIL import Image

import argparse
import json
#import mailboxManager

from datetime import datetime
from threading import Lock

# ### Potentiometer Imports ### ### ### ### ### ### ### ### ###
# import sys
# import time
# # By appending the folder of all the GrovePi libraries to the system path here,
# # we are successfully `import grovepi`
# sys.path.append('../../Software/Python/')
# # This append is to support importing the LCD library.
# sys.path.append('../../Software/Python/grove_rgb_lcd')

# import grovepi
# from grove_rgb_lcd import *
# ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ###

# import pickle

app = Flask('RaspberryPi Mailbox Server')

@app.route('/send_image', methods=['POST'])
def post_image_callback():
    # # Check if an image is in the request
    # if 'image' not in request.files:
    #         return jsonify({"error": "No image file in request"}), 400
    # Ensure the content type is JPEG
    if request.content_type != 'image/jpeg':
            return jsonify({"error": "Invalid content type. Only JPEG is supported."}), 400
    # # Retrieve the image
    # image_file = request.files['image']
    
    # # Save the image locally (optional)
    # raw_path = f'uploads/{image_file.filename}'
    # save_path = f'uploads/{image_file.filename}.jpg'
    # image_file.save(raw_path)

    # Save the image data
    image_data = request.data
    save_path = f'uploads/test_image.jpg'
    with open(save_path, "wb") as f:
            f.write(image_data)

    return jsonify({"message": f"Image received and saved as {save_path}"}), 200


# Define image pre-processing in a function
def image_preprocessor(image_path):
  img = Image.open(image_path).convert('L')
  img = img.resize(size=(128, 128))
  img_array = (np.array(img) > 100)*255  # Convert to a numpy array
  plt.imshow(img_array)

  img_array = img_array / 255.0  # Normalize pixel values to [0, 1]
  img_array = img_array.reshape(1, 128, 128, 1)  # Reshape for model input
                # (batch_size, image dimension, single channel grayscale)


if __name__ == '__main__':
    # app.run(debug=True, host='0.0.0.0', port=5000) #For VM
    # app.run(debug=True, host='127.0.0.1', port=5000)
    # app.run(debug=True, host='172.26.242.207', port=8080)
    app.run(debug=True, host='0.0.0.0', port=8080)

    # ## Potentiometer code from lab2.py ## 
    # potentiometer = 0
    # # PORT = 4    # D4 -- this was for the ultrasonic in Lab 2
    # grovepi.pinMode(potentiometer, "INPUT")
    # time.sleep(1)
    # # prev_distance = 0

    # while True:
    #     potentRead = int((grovepi.analogRead(potentiometer)) # read the potentiometer value

    #     # range of GrovePi potentiometer= 0 - 1023
    #     if (  int(grovepi.analogRead(potentiometer)) < 512):
    #         # Turn on RED LED
    #         print("Red LED on")
    #     else:
    #         print("Blue LED on")       
                         
    #     time.sleep(0.2)    
    # ## END of Potentiometer code from lab2.py ## 
