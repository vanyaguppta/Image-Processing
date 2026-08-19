import cv2

# 1. Load your image
# Replace 'your_image.jpg' with your actual file path
image = cv2.imread('Sweets.jpg')

# 2. Apply Gaussian Blur
# (15, 15) is the kernel size (width, height). Higher numbers = more blur.
# 0 lets OpenCV calculate the standard deviation automatically based on kernel size.
blurred_image = cv2.GaussianBlur(image, (15, 15), 0)

# 3. Save or display the result
cv2.imwrite('blurred_opencv.jpg', blurred_image)

# Optional: Display the image in a window (press any key to close)
cv2.imshow('Gaussian Blur(Vanya-CS24058)', blurred_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
