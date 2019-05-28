import face_recognition
import glob
import re
import pickle

path = './known_data/'
dist_name = 'known_data.pkl'


def load():
    with open(path + dist_name, 'rb') as known_data:
        names, known_face_encodings = pickle.load(known_data)
    return list(names), list(known_face_encodings)


def save():
    fileNames = glob.glob(path + '*.jpg')
    names = map(lambda fileName: re.match(
        r'^.*known_data/(.*)\.jpg', fileName).group(1), fileNames)
    images = map(
        lambda filePath: face_recognition.load_image_file(
            filePath), fileNames)
    known_face_encodings = map(
        lambda image: face_recognition.face_encodings(image)[0], images)
    with open(path + dist_name, 'wb') as known_data:
        pickle.dump((list(names), list(known_face_encodings)), known_data)
