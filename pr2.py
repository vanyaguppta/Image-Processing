import cv2
import numpy as np
import matplotlib.pyplot as plt
img=cv2.imread("rabbit.jpg")
plt.imshow(img)
plt.title("Vanya")
plt.waitforbuttonpress()
plt.close('all')


# BRG to RGB
import cv2
# import numpy as np
import matplotlib.pyplot as plt
img=cv2.imread("rabbit.jpg")
# Converting BGR to RGB
RGB_img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
plt.imshow(RGB_img)
plt.title("Vanya-CS24058")
plt.waitforbuttonpress()
plt.close('all')

import cv2
path=r"C:\Users\Student\PycharmProjects\Vanya\rabbit.jpg"
img=cv2.imread(path,cv2.IMREAD_GRAYSCALE)
cv2.imshow("Vanya-CS24058",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2
import numpy as np
image1 = cv2.imread('sacred-forest.jpg')
image2 = cv2.imread('rabbit.jpg')
weightedSum = cv2.addWeighted(image1, 0.5, image2, 1, 0)
cv2.imshow('Weighted Image(Vanya-CS24058)', weightedSum)
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()

import cv2
import numpy as np
image1 = cv2.imread('rabbit.jpg')
image2 = cv2.imread('sacred-forest.jpg')
sub = cv2.subtract(image1, image2)
cv2.imshow('Subtracted Image(Vanya-CS24058)', sub)
# De-allocate any associated memory usage
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()

import cv2
import numpy as np
img1 = cv2.imread('rabbit.jpg')
img2 = cv2.imread('sacred-forest.jpg')
dest_and = cv2.bitwise_and(img2, img1, mask = None)
cv2.imshow('Bitwise And(Vanya-CS24058)', dest_and)
# De-allocate any associated memory usage
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()

import cv2
import numpy as np
img1 = cv2.imread('sacred-forest.jpg')
img2 = cv2.imread('rabbit.jpg')
dest_or = cv2.bitwise_or(img2, img1, mask=None)
cv2.imshow('Bitwise OR(Vanya-CS24058)', dest_or)
# De-allocate any associated memory usage
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()

import cv2
import numpy as np
img1 = cv2.imread('rabbit.jpg')
img2 = cv2.imread('sacred-forest.jpg')
dest_xor = cv2.bitwise_xor(img1, img2, mask = None)
cv2.imshow('Bitwise XOR(Vanya-CS24058)', dest_xor)
# De-allocate any associated memory usage
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()


import cv2
import numpy as np
img1 = cv2.imread('sacred-forest.jpg')
img2 = cv2.imread('rabbit.jpg')
dest_not1 = cv2.bitwise_not(img1, mask = None)
dest_not2 = cv2.bitwise_not(img2, mask = None)
cv2.imshow('Bitwise NOT on Forest(Vanya-CS24058)', dest_not1)
cv2.imshow('Bitwise NOT on Rabbit(Vanya-CS24058)', dest_not2) # De-allocate any associated memory usage
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()


