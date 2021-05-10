'''In Development'''

from PIL import Image
import glob
import os
import face_recognition


top, right, bottom, left = face_location

image_list = []
n = 0

path, dirs, files = next(os.walk('/home/pi/tflite1/images/'))
file_count = len(files)

for Imagename in glob.glob('/home/pi/tflite1/images/*.jpg'):
    image=face_recognition.load_image_file(Imagename)
    image_list.append(image)

    n += 1

    print('Analyzing image %s of %s' % (n, file_count))
    face_locations = face_recognition.face_locations(image, number_of_times_to_upsample=0, model="cnn")

    print("I found {} face(s) in this photograph.".format(len(face_locations)))

    top, right, bottom, left = face_location

    # You can access the actual face itself like this:
    face_image = image[top:bottom, left:right]
    pil_image = Image.fromarray(face_image)
    pil_image.show()


