import cv2 
import numpy as np 

# Create a black image (zeros)
img = np.zeros((512,512,3), np.uint8)
print(img.shape)  # Should print (512, 512, 3)

# Make entire image blue (BGR format: 255,0,0 = Blue)
img[:] = (255, 0, 0)  # This will make the whole image blue

### Create a line (uncomment to use)
# cv2.line(img, (0,0), (300,400), (0,255,0), 5)  # Green line

### Rectangle (uncomment to use)
# cv2.rectangle(img, (100,50), (250,350), (0,0,255), 7)  # Red rectangle

### Create circle (uncomment to use)
# cv2.circle(img, (400,50), 50, (0,0,255), 4)  # Red circle
# OR filled circle:
# cv2.circle(img, (400,50), 50, (0,0,255), cv2.FILLED)

### Put text - This should work now!
cv2.putText(img, "Nur Nafis Fuad", (200,440), cv2.FONT_HERSHEY_DUPLEX, 1, (0,255,0), 1)

cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()