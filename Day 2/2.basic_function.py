import cv2

### 1. convert color image to grayscale
# img = cv2.imread("resources/lena.png")
# img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# print(img.shape)
# print(img_gray.shape)

# cv2.imshow("Original Image", img)
# cv2.imshow("Grayscale Image", img_gray)
# cv2.waitKey(0)

### 1. convert to blur image
img = cv2.imread("resources/lena.png")
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_blur = cv2.GaussianBlur(img_gray, (7, 7), 0)

print(img.shape)
print(img_gray.shape)
print(img_blur.shape)

cv2.imshow("Original Image", img)
cv2.imshow("Grayscale Image", img_gray)
cv2.imshow("Blurred Image", img_blur)
cv2.waitKey(0)