import os
import io
import cv2
import datetime

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types


credential_path = "C:/Users/moeoi/Desktop/jasmine-dev-d6c5b7b4426b.json"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path


name = "photo_" + datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
path = "C:/Users/moeoi/Desktop/image/" + name + ".png"

capture = cv2.VideoCapture(0)

# 取得した画像データは変数imageに格納。retは取得成功変数。
ret, image = capture.read()

if ret == True:
    cv2.imwrite(path, image)
    print("Photo was taken properly")


# Instantiates a client
client = vision.ImageAnnotatorClient()

# The name of the image file to annotate
file_name = os.path.join(
    os.path.dirname(__file__), path)

# Loads the image into memory
with io.open(file_name, 'rb') as image_file:
    content = image_file.read()

image = types.Image(content=content)

# Performs label detection on the image file
response = client.face_detection(image=image)
faces = response.face_annotations
print(faces)
