'''
File: facial_encoder.py
Authors: Cameron Slupeiks, Nicole Laurin
Date: 04/04/21
'''

from imutils import paths
import cv2
import os
import pickle
import face_recognition


def encode_faces(images):

    # Create empty lists to store facial
    # encodings and person names.
    encodings = []
    names = []

   # Loop over each image, extract the person name
   # from image path, and compute facial encodings.
    for (i, path) in enumerate(images):
        bgr_image = cv2.imread(path)
        rgb_image = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2RGB)
        faces = face_recognition.face_locations(rgb_image, model='hog')
        embeddings = face_recognition.face_encodings(rgb_image, faces)
        name = path.split(os.path.sep)[-2]

        for embedding in embeddings:
            encodings.append(embedding)
            names.append(name)

    # Create dictionary of encodings and person names.
    data = {'encodings': encodings, 'names': names}

    return data


def main():

    # Create encodings directory.
    if os.path.isdir('encodings') is False:
        os.mkdir('encodings')

    # Get path to image dataset.
    images = list(paths.list_images('images'))

    # Generate facial encodings.
    data = encode_faces(images)

    # Write data to a pickle file in encodings directory.
    filepath = 'encodings/faces.pickle'
    f = open(filepath, 'wb')
    f.write(pickle.dumps(data))
    f.close()


if __name__ == '__main__':
    main()
