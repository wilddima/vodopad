import face_recognition
import cv2
import os
import re
import pdb
try:
    import matplotlib.pyplot as plt
except:
    pass

image_ext = re.compile(r'\.JPG|\.jpg|\.jpeg|\.JPEG|\.PNG|\.png')

class DlibFaceIdentifier:
    def __init__(self, reference_path, debug=False):
        self.reference_image_pathes = []
        self.reference_images = []
        self.known_faces = []
        self.known_names = []
        self.known_encodings = []
        self.debug = debug

        if os.path.isdir(reference_path):
            for path in os.listdir(reference_path):
                extension = os.path.splitext(path)[1]
                if image_ext.match(extension):
                    self.reference_image_pathes.append(reference_path + '/' + path)
        else:
            self.reference_image_pathes = [reference_path]

        for image_path in self.reference_image_pathes:
            image = self.load_image(image_path)
            encoding = face_recognition.face_encodings(image)[0]

            self.known_faces.append(image)
            self.known_encodings.append(encoding)
            self.known_names.append(os.path.basename(image_path).split('.')[0])

            self.reference_images.append({'image': image,
                                          'encoding': encoding,
                                          'name': os.path.basename(image_path)})

    def identify(self, image_path):
        image = self.load_image(image_path)
        locations = face_recognition.face_locations(image)
        encodings = face_recognition.face_encodings(image, locations)
        result = {}
        if self.debug:
            self.show_recognized_image(image, locations, encodings)
        for face_encoding in encodings:
            matches = face_recognition.compare_faces(self.known_encodings, face_encoding)
            for k, v in zip(self.known_names, matches):
                if not result.get(k):
                    result[k] = v

        return(image_path, result)

    def load_image(self, path):
        return face_recognition.load_image_file(path)

    def load_encoding(self, image):
        return face_recognition.face_encoding(image)[0]

    def show_recognized_image(self, image, locations, encodings):
        for (top, right, bottom, left), face_encoding in zip(locations, encodings):
            matches = face_recognition.compare_faces(self.known_encodings, face_encoding)
            cv2.rectangle(image, (left, top), (right, bottom), (255,0,0),2)
            name = "Unknown"
            if True in matches:
                first_match_index = matches.index(True)
                name = self.known_names[first_match_index]
            cv2.putText(image, name, (left, bottom + 100), cv2.FONT_HERSHEY_SIMPLEX, 2,(255,255,255),2)
        plt.rcParams['figure.figsize'] = 18,10
        plt.imshow(image)
        plt.title('Image', fontsize=15)
        plt.axis('off')
        plt.show()
