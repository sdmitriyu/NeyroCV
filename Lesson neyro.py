import cv2
# import numpy as np
#
# kernel = np.ones((5, 5), np.uint8)
# # Вывод картинки
# img = cv2.imread('images/73338.jpg')
# new_img = cv2.resize(img, (img.shape[1] // 5, img.shape[0] // 5))
# new_img = cv2.GaussianBlur(new_img, (20, 20), 0)
# new_img = cv2.cvtColor(new_img, cv2.COLOR_BGR2GRAY) # Картинка в сером формате с одним слоем
# new_img = cv2.Canny(new_img, 90, 90) # Картинка в бинарном формате
# new_img = cv2.dilate(new_img, kernel, iterations=1) # Обводка
# new_img = cv2.erode(new_img, kernel, iterations=cv2. обрезать картинку1)
# cv2.imshow('klava', new_img[0:200, 0:500]) # Обрезка картинки по пикселям
# cv2.waitKey(5000)
# print(new_img.shape)
#
#
#
#
# Вывод видео
# cap = cv2.VideoCapture('images/Untitled Project.mp4')
# while True:
#     success, img = cap.read()
#     img = cv2.GaussianBlur(img, (9, 9), 0)
#     img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # Картинка в сером формате с одним слоем
#     img = cv2.Canny(img, 30, 30) # Картинка в бинарном формате
#     img = cv2.dilate(img, kernel, iterations=1)
#     img = cv2.erode(img, kernel, iterations=1)
#     cv2.imshow('Result', img)
#     if cv2.waitKey(10) & 0xFF == ord('q'):
#         break
#
# Вывод веб-камеры ноутбука
# cap = cv2.VideoCapture(0)
# cap.set(3, 500)
# cap.set(4, 300)
#
# while True:
#     success, img = cap.read()
#     cv2.imshow('Result', img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#
# отзеркаливание картинки
# img = cv2.imread('images/73338.jpg')
# img = cv2.resize(img, (img.shape[1] // 5, img.shape[0] // 5))
# # img = cv2.flip(img, -1)
#
# # Вращение картинки
# def rotate(img_param, angle):
#     heiht, width = img_param.shape[:2]
#     point = (heiht // 2, width // 2)
#
#     mat = cv2.getRotationMatrix2D(point, angle, 1)
#     return cv2.warpAffine(img_param, mat, (width, heiht))
#
# img = rotate(img, 90)
#
# # Смещение (трансформирование) картинки
# def transform(img_param, x, y):
#      mat = np.float32([[1, 0, x], [0, 1, y]])
#      return cv2.warpAffine(img_param, mat, (img_param.shape[1], img.shape[0]))
#
# img = transform(img, 30, 20)
#
#
#
# img = cv2.imread('images/73338.jpg')
# new_img = np.zeros(img.shape, dtype='uint8')
# img = cv2.resize(img, (img.shape[1] // 5, img.shape[0] // 5))
# img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# img = cv2.GaussianBlur(img, (5, 5), 0)
# img = cv2.Canny(img, 100, 140)
# con, hir = cv2.findContours(img, cv2.RETR_LIST, cv2. CHAIN_APPROX_NONE)
# cv2.drawContours(new_img, con, -1, (230, 111, 148), 1)
#
# print(con)
#
# cv2.imshow('klava', new_img)
# cv2.waitKey(5000)


img = cv2.imread('images/73338.jpg')
img = cv2.resize(img, (img.shape[1] // 5, img.shape[0] // 5))
# img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# img = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
r, g, b, = cv2.split(img) # Разделение картинки на слои
img = cv2.merge(b, g, r) # Соединение слоёв картинки
cv2.imshow('klava', img)
cv2.waitKey(5000)