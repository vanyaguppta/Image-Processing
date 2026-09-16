# Python program to read image as YCrCb color space

# Import cv2 module
import cv2

# Read the image
img = cv2.imread("images.jfif")

# Check if image is loaded properly
if img is None:
    print("Error: Image not found or unable to load.")
else:
    # Convert to YCrCb color space
    img = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)

    # Show the image
    cv2.imshow("image", img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()