import cv2
import numpy as np 


width , height = 250, 350


img = cv2.imread("resources/cards.jpg")


pts1 = np.float32([[752,118],[1120,265],[540,668],[871,830]])

pts2 = np.float32([[0,0], [width, 0], [0,height], [width, height]])
# This is the destination points for the perspective transform
# This will map the corners of the card to a flat rectangle of size (width, height)

metrix = cv2.getPerspectiveTransform(pts1, pts2) #metrix = cv2.getPerspectiveTransform(pts1, pts2) This function computes the perspective transformation matrix that maps the points in pts1 to the corresponding points in pts2. The resulting matrix can then be used to perform the perspective transformation on the image.
img_out = cv2.warpPerspective(img, metrix, (width, height)) #img_out = cv2.warpPerspective(img, metrix, (width, height)) Here, metrix is the transformation matrix obtained from cv2.getPerspectiveTransform, and (width, height) specifies the size of the output image.
# This applies the perspective transformation to the image, resulting in a warped image of the card that is now flat and has the specified width and height.

cv2.imshow('cards', img)
cv2.imshow('cards_warp', img_out)


cv2.imshow('cards', img)
cv2.waitKey(0)
