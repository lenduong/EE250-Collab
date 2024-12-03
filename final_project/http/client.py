import requests
import cv2

if __name__ == '__main__':
        url = "http://192.168.91.71:5000/send_image"
        # url = "http://172.26.240.1:5000/send_image"
        # url = "http://172.26.242.207:5000/send_image"
        
        # Start recording
        cam = cv2.VideoCapture(0)
        
        #while True:
        ret, image = cam.read()
        #cv2.imshow('Imagetest',image)
        #k = cv2.waitKey(1)
        #if k != -1:
        #break
        
        #image_path = r'~/ee250_fp_grish_le/testing/testimage.jpg'
        #image = cv2.imread(image_path)
        
        # cv2.imwrite('./testing/testimage2.jpg', image)
        cam.release()
        # ----------------------------------
        # # Open the image file in binary mode
        # # with open("your_image.jpg", "rb") as image_file:
        # # files = {"image": image_file}
        # files = {"image": image}
        
        # # Send the POST request
        # response = requests.post(url, files=files)

        _, buffer = cv2.imencode('.jpg', image)

        # Send the image via HTTP POST
        headers = {"Content-Type": "image/jpeg"}  # Indicate JPEG format
        response = requests.post(url, data=buffer.tobytes(), headers=headers)
        
        # Check the response status code
        if response.status_code == 200:
            print("Image uploaded successfully")
        else:
            print("Error uploading image:", response.status_code)
