import cv2
import numpy as np

width , height = 250, 350

# img = cv2.imread("resources/cards.jpg")
img = cv2.imread("resources/docs.jpg")

# pts1 = np.float32([[752,188],[1120,265],[540,668],[871,830]])
pts1 = np.float32([[317,270],[731,268],[222,865],[728,864]])
pts2 = np.float32([[0,0], [width,0], [0,height], [width,height]]) # Formulaff

metrix = cv2.getPerspectiveTransform(pts1, pts2)
img_out = cv2.warpPerspective(img, metrix, (width, height))

cv2.imshow('cards', img)
cv2.imshow('cards_warp', img_out)

cv2.imshow('cards', img)
cv2.waitKey(0)