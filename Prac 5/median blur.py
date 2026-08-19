import cv2
import numpy
import matplotlib.pyplot as plt

img = cv2.imread("Noisy.jpg")
plt.imshow(img)

# Apply Median Filter (5 is the kernel size, must be an odd integer)
dst = cv2.medianBlur(img, 5)

cv2.imshow('Median BLUR:- Vanya-CS24058', numpy.hstack((img, dst)))
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)
