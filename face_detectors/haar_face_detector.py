import cv2
import matplotlib.pyplot as plt

def detect_face(imagepath):
    face_cascade = cv2.CascadeClassifier('vendor/haarcascade_frontalface_default.xml')
    image = cv2.imread(imagepath)
    gray  = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)

    plt.rcParams['figure.figsize'] = 18,10
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title('Image', fontsize=15)
    plt.axis('off')
    plt.show()
