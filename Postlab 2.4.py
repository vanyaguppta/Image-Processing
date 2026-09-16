import cv2

# Read the image
image = cv2.imread("images.jfif")

# Check if image was loaded successfully
if image is None:
    print("Error: Image not found or failed to load.")
    exit()

# Convert the image to LAB color space
lab_image = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)

# Display the LAB image
cv2.imshow("LAB Image", lab_image)

# Wait for a key press and close all OpenCV windows
cv2.waitKey(0)
cv2.destroyAllWindows()