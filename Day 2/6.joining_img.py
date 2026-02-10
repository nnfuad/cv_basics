import cv2
import numpy as np

img = cv2.imread("resources/lena.png")

img_hor = np.hstack((img, img)) 
# np.hstack() is a function in NumPy that horizontally stacks arrays. 
# In this case, it takes the image 'img' and stacks it with itself horizontally, 
# resulting in a new image that is twice the width of the original. 

img_var = np.vstack((img, img))
# np.vstack() is a function in NumPy that vertically stacks arrays. 
# In this case, it takes the image 'img' and stacks it with itself vertically, 
# resulting in a new image that is twice the height of the original.

cv2.imshow("Horizontal", img_hor)
cv2.imshow("Vertical", img_var)
cv2.waitKey(0)