import cv2

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades +
    "haarcascade_frontalface_default.xml"
)

def detect_faces():

    cap = cv2.VideoCapture(0)

    ret, frame = cap.read()

    if not ret:
        cap.release()
        return 0

    gray = cv2.cvtColor(
        frame,
        cv2.COLOR_BGR2GRAY
    )

    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=5
    )

    count = len(faces)

    print("Faces detected:", count)

    cap.release()

    return count