import sys
import numpy as np
import tensorflow as tf
import tensorflow.keras as keras
from PIL import Image
import matplotlib.pyplot as plt

print("Arguments: ")
print(sys.argv)

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

if __name__ == '__main__':
  # Load the model from the header file
  # Load the trained model
  loaded_model = keras.models.load_model('handNums_model-1104.h5')

  # Find the hand number image the model should read/predict
  # image_path = 'g_1.png'
  image_path = '/mnt/c/Users/leduo/Desktop/EE250-Collab/final_project/capturing_single_image/g_5.png'
  # if len(sys.argv) > 0:
  #   image_path = sys.argv[0]

  img_array = image_preprocessor('1003_4.png')
  prediction = loaded_model(img_array) # use a direct call for small input size
  predict_value = np.argmax(prediction)
  
  print("Model Prediction: ")
  print(predict_value)
  
  # Taking model output and converting it to be ON or OFF for LEDs
  if predict_value % 2 == 0:
    print("LED ON")
  else:
    print("LED OFF")
