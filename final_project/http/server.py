from flask import Flask
from flask import jsonify
from flask import request
from PIL import Image

# Imports for loading the ML model #
import numpy as np
import tensorflow as tf
import tensorflow.keras as keras
from PIL import Image
import matplotlib.pyplot as plt

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
loaded_model = keras.models.load_model('handNums_model-1104.h5')
trial_count = 0

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
        
    LED_command = deploy()
    
    return jsonify({"message1": f"Image received and saved as {save_path}", "message2":LED_command}), 200


# Define image pre-processing in a function
def image_preprocessor(image_path):
  img = Image.open(image_path).convert('L')
  img = img.resize(size=(128, 128))
  img_array = (np.array(img) > 100)*255  # Convert to a numpy array
  plt.imshow(img_array)

  img_array = img_array / 255.0  # Normalize pixel values to [0, 1]
  img_array = img_array.reshape(1, 128, 128, 1)  # Reshape for model input
                # (batch_size, image dimension, single channel grayscale)
  return img_array

def deploy():
    image_path = '/mnt/c/Users/leduo/Desktop/EE250-Collab/final_project/http/uploads/test_image.jpg'
    img_array = image_preprocessor(image_path)
    prediction = loaded_model(img_array) # use a direct call for small input size
    predict_value = np.argmax(prediction)

    print("Model Prediction: ")
    print(predict_value)

    # Taking model output and converting it to be ON or OFF for LEDs
    # if predict_value % 2 == 0:
    #     print("LED ON")
    #     return True
    # else:
    #     print("LED OFF")
    #     return False
    global trial_count
    print("count: ", trial_count)
    if trial_count %2 == 0:
        return True
        trial_count += 1
    else:
        return False
        trial_count += 1


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)

    # # Load the trained model from the header file
    # loaded_model = keras.models.load_model('handNums_model-1104.h5')

    
