import cv2

# Загрузка каскада Хаара для распознавания глаз
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

# Захват видеопотока с камеры
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    # Преобразование в черно-белое изображение для ускорения работы алгоритма
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Детекция глаз с помощью каскада Хаара
    eyes = eye_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Размытие области глаз
    for (x, y, w, h) in eyes:
        roi = frame[y:y + h, x:x + w]
        roi = cv2.GaussianBlur(roi, (25, 25), 0)  # применение размытия
        frame[y:y + h, x:x + w] = roi

    # Вывод обработанного кадра
    cv2.imshow('Blurred Eyes', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
# cv2.destroyAllWindows()
