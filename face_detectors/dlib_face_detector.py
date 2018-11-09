import cv2
import matplotlib.pyplot as plt

def detect_face(imagepath):
    image = face_recognition.load_image_file(imagepath)
    faces = face_recognition.face_locations(image)
    for (top, right, bottom, left) in faces:
        cv2.rectangle(image, (left, top), (right, bottom), (255,0,0),2)

    plt.rcParams['figure.figsize'] = 18,10
    plt.imshow(image)
    plt.title('Image', fontsize=15)
    plt.axis('off')
    plt.show()
