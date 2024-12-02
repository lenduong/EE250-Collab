import sys
import numpy as np
import tensorflow as tf
import tensorflow.keras as keras
from PIL import Image

print("Arguments: ")
print(sys.argv)

def image_preprocess(image_path):
  img = Image.open(image_path)
  plt.imshow(img)
  img = img.convert('L')  # Convert to grayscale
  img = img.resize(size=(128, 128))
  img_array = np.array(img)  # Convert to a numpy array
  img_array = img_array / 255.0  # Normalize pixel values to [0, 1]
  img_array = img_array.reshape(1, 128, 128, 1)  # Reshape for model input
                # parameters: (batch_size, image dimension, single channel grayscale)
  return img_array

if __name__ == '__main__':
  # Load the model from the header file
  loaded_model = keras.models.load_model('handNums_model.h5')

  # Find the hand number image the model should read/predict
  image_path = 'g_1.png'
  if len(sys.argv) > 0:
    image_path = sys.argv[0]
  
  prediction = loaded_model(image_preprocess(image_path)) # use a direct call for small input size
  print("Model Prediction: ")
  print(np.argmax(prediction))
