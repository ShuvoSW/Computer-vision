import cv2

### 1. convert color image to grayscale
img = cv2.imread("resources/lena.png")
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

print(img.shape)
print(img_gray.shape)

cv2.imshow("Original Image", img)
cv2.imshow("Grayscale Image", img_gray)
cv2.waitKey(0)
