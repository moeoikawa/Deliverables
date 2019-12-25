import os
import io
# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types


credential_path = "C:/Users/moeoi/Desktop/jasmine-dev-d6c5b7b4426b.json"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path


# Instantiates a client
client = vision.ImageAnnotatorClient()

# The name of the image file to annotate
file_name = os.path.join(
    os.path.dirname(__file__),
    'C:/Users/moeoi/Desktop/photos/test.jpg')

# Loads the image into memory
with io.open(file_name, 'rb') as image_file:
    content = image_file.read()

image = types.Image(content=content)

# Performs label detection on the image file
response = client.face_detection(image=image)
#color = client.image_properties(image=image)
#print(faces)
#print(color)


faces = response.face_annotations
face1 = faces[0]
face2 = faces[1]

"""
joy_likelihood: 楽しい
sorrow_likelihood: 悲しい
anger_likelihood: 怒っている
surprise_likelihood: 驚いている
under_exposed_likelihood: 露光不足
blurred_likelihood: ぼやけている
headwear_likelihood: 帽子を被っている

VERY_UNLIKELY: 1
UNLIKELY: 2
POSSIBLE: 3
LIKELY: 4
VERY_LIKELY: 5
"""
print("1人目：")
print(face1.joy_likelihood)
print("2人目：")
print(face2.joy_likelihood)
print((face1.joy_likelihood)-(face2.joy_likelihood))

if (face1.joy_likelihood) - (face2.joy_likelihood) == 0:
    print("相性100%")
elif (face1.joy_likelihood) - (face2.joy_likelihood) == 1 or (face1.joy_likelihood) - (face2.joy_likelihood) == -1:
    print("相性90%")
elif (face1.joy_likelihood) - (face2.joy_likelihood) == 2 or (face1.joy_likelihood) - (face2.joy_likelihood) == -2:
    print("相性80%")
elif (face1.joy_likelihood) - (face2.joy_likelihood) == 3 or (face1.joy_likelihood) - (face2.joy_likelihood) == -3:
    print("相性70%")
elif (face1.joy_likelihood) - (face2.joy_likelihood) == 4 or (face1.joy_likelihood) - (face2.joy_likelihood) == -4:
    print("相性60%")
elif (face1.joy_likelihood) - (face2.joy_likelihood) == 5 or (face1.joy_likelihood) - (face2.joy_likelihood) == -5:
    print("相性50%")
