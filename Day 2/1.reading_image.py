import cv2

## Reading images

# img = cv2.imread("resources/lena.png")

# # print(img.shape)
# cv2.imshow("Output", img)
# cv2.waitKey(0)

## Reading videos

# cap = cv2.VideoCapture("resources/elon.mp4")
# print(cap)

# while True:
#     success, img = cap.read()
#     print(img.shape)
#     cv2.imshow("Output", img)
    
#     if cv2.waitKey(1) & 0xff == ord('q'):
#         break
    
## Reading from webcam

cap = cv2.VideoCapture(0)

cap.set(3, 640)  # width
cap.set(4, 480)  # hight

while True:
    success, img = cap.read()
    cv2.imshow("Output", img)
    
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
        