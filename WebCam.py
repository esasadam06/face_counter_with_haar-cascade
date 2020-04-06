

import cv2
face_cascade = cv2.CascadeClassifier('haarcascade-frontalface-default.xml')
people=0


def detect(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    people = 0
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
        cv2.putText(frame, 'Detected', (x+w, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1, cv2.LINE_AA)
        people = people + 1
    cv2.putText(frame, 'Detected People :' + str(people) + " ", (35, 35), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1,cv2.LINE_AA)
    return frame


video_capture = cv2.VideoCapture(0)
while True:
    _, frame = video_capture.read()
    canvas = detect(frame)
    cv2.imshow('Video', canvas)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
video_capture.release()
cv2.destroyAllWindows()