import cv2

eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    eyes = eye_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in eyes:
        roi = frame[y:y + h, x:x + w]
        roi = cv2.GaussianBlur(roi, (25, 25), 0)
        frame[y:y + h, x:x + w] = roi

    cv2.imshow('Blurred Eyes', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
# cv2.destroyAllWindows()
