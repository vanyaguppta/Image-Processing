# Python code to read image
import cv2
img = cv2.imread("butterfly.png", cv2.IMREAD_COLOR)
cv2.imshow("VANYA", img)
cv2.waitKey(0)
# 0 in the above statement means the image will be shown for how long user does not closes it
cv2.destroyAllWindows()

