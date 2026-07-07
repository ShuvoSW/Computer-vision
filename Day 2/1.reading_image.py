import cv2

## Reading images

img = cv2.imread("resources/lena.png")

print(img.shape)
cv2.imshow("Output", img)
cv2.waitKey(0)