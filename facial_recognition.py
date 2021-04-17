'''
File: facial_recognition.py
Authors: Cameron Slupeiks, Nicole Laurin
Date: 04/04/21
'''

import cv2
import os
import pickle
import imutils
import face_recognition


def verify_faces(data, video_capture):

    # List of identified face names.
    names = []

    # Set drawing variables.
    font = cv2.FONT_HERSHEY_SIMPLEX
    filled = cv2.FILLED
    color = (255, 0, 0)
    text = (255, 255, 255)
    thickness = 2
    size = 0.6

    # Capture frame from livestream.
    ret, frame = video_capture.read()

    # Convert frame from BGR to RGB.
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Resize RGB frame to speed up processing.
    rgb_scaled = imutils.resize(frame, width=400)

    # Use hog cnn to detect faces in rgb frame.
    faces = face_recognition.face_locations(rgb_scaled,
                                            model='hog')

    # Compute facial encodings from detected faces.
    encodings = face_recognition.face_encodings(rgb_scaled, faces)

    # Loop over facial encodings from frame.
    for encoding in encodings:

        # Set face name to `Unknown` as it has not been identified yet.
        name = 'Unknown'

        # Compare encodings from frame with encodings from faces.pickle.
        matches = face_recognition.compare_faces(data['encodings'],
                                                 encoding)

        # A match has been found.
        if True in matches:
            matched_indexes = [i for (i, j) in enumerate(matches) if j]
            counts = {}

            # Iterate over matches and increment count.
            for i in matched_indexes:
                name = data['names'][i]
                counts[name] = counts.get(name, 0) + 1

            # Find name with the most matches.
            name = max(counts, key=counts.get)

        # Append face name to list of names.
        names.append(name)

        # Loop over matched face(s).
        for (top, right, bottom, left), name in zip(faces, names):

            # If face is not recognized, set color to red.
            if name == 'Unknown':
                color = (0, 0, 255)

            # Otherwise, capitalize first and last name.
            else:
                name_list = name.split('_')
                name = name_list[0].capitalize() + ' ' + \
                    name_list[1].capitalize()

            # Since frame for face detection was scaled
            # down to 200px, scale up face locations.
            scale = frame.shape[1] / float(rgb_scaled.shape[1])
            top = int(top * scale)
            right = int(right * scale)
            bottom = int(bottom * scale)
            left = int(left * scale)

            # Draw rectangle(s) around predicted face(s).
            cv2.rectangle(frame, (left, top),
                          (right, bottom), color, thickness)

            # Draw label(s) around name(s).
            cv2.rectangle(frame, (left, top),
                          (right, top - 35), color, filled)
            cv2.putText(frame, name, (left, top - 10), font,
                        size, text, thickness)

    return frame


def main():

    # Load facial encodings.
    if os.path.exists(os.path.join(os.getcwd(), 'encodings', 'faces.pickle')):
        data = pickle.loads(open('encodings/faces.pickle', 'rb').read())
    else:
        print('Error: facial encodings do not exist. Please run facial_encoder.py.')
        exit(1)

    # Start livestream.
    video_capture = cv2.VideoCapture(0)

    # Loop over each frame in video stream and compute facial recognition.
    while True:

        # Verify faces.
        frame = verify_faces(data, video_capture)

        # Display frame window.
        cv2.imshow('Facial Verification', frame)

        # Set exit key to `q`.
        key = cv2.waitKey(1) & 0xFF

        # User has chosen to exit.
        if key == ord('q'):
            break

    # End livestream and destroy all windows.
    video_capture.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
