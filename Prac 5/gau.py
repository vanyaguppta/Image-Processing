import cv2
import numpy
from matplotlib import pyplot as plt

# using imread()
img = cv2.imread("Sweets.jpg")
plt.imshow(img)
dst = cv2.GaussianBlur(img, (5, 5), cv2.BORDER_DEFAULT)
cv2.imshow('Vanya-CS24058', numpy.hstack((img, dst)))
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)
