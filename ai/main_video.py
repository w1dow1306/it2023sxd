import cv2
from simple_facerec import SimpleFacerec
# Encode faces from a folder
sfr = SimpleFacerec()
sfr.load_encoding_images("images/")

# Load Camera
cap = cv2.VideoCapture(0)

# Open the text file for writing
with open("data.txt", "w") as f:
    while True:
        ret, frame = cap.read()

        # Detect Faces
        face_locations, face_names = sfr.detect_known_faces(frame)
        for face_loc, name in zip(face_locations, face_names):
            y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]

            cv2.putText(frame, name, (x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (90, 0, 200), 2)
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 200), 4)

            # Write the recognized name to the text file
            f.write(name + "\n")

        cv2.imshow("Frame", frame)

        key = cv2.waitKey(1)
        if key == 27:  # Press Esc key to exit
            break
        elif key == ord('0'):  # Press 0 key to stop
            break
    
# Close the camera and text file
cap.release()
cv2.destroyAllWindows()
