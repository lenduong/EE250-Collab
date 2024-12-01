from flask import Flask
from flask import jsonify
from flask import request
from PIL import Image

import argparse
import json
#import mailboxManager

from datetime import datetime
from threading import Lock

# import pickle

app = Flask('RaspberryPi Mailbox Server')

@app.route('/send_image', methods=['POST'])
def post_image_callback():
        # Check if an image is in the request
        if 'image' not in request.files:
                return jsonify({"error": "No image file in request"}), 400
        
        # Retrieve the image
        image_file = request.files['image']
        
        # Save the image locally (optional)
        raw_path = f'uploads/{image_file.filename}'
        save_path = f'uploads/{image_file.filename}.jpg'
        image_file.save(raw_path)

        with Image.open(raw_path) as img:
                # Convert to RGB mode (JPEG doesn't support transparency)
                img = img.convert("RGB")
                
                # Save the image as JPEG
                img.save(save_path, "JPEG")
    
        return jsonify({"message": f"Image {image_file.filename} received and saved at {save_path}"}), 200

if __name__ == '__main__':
        app.run(debug=True, host='0.0.0.0', port=5000)
