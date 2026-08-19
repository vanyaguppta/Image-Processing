import cv2
import numpy as np

# -------------------------------
# PART 1: Generate mask & restore using TELEA
# -------------------------------
# Step 1: Read the damaged image
damaged_img = cv2.imread("frog.jpg")

# Safeguard against file path or loading errors
if damaged_img is None:
    raise FileNotFoundError("Could not open or find 'frog.jpg'. Check the file path.")

# Step 2: Create mask from damaged image using fast, vectorized NumPy operations
# Find all pixels where the sum of channels is exactly 0 (pure black)
is_black = np.sum(damaged_img, axis=2) == 0

# Create a single-channel grayscale mask directly (0 = black)
mask_gray = np.zeros(damaged_img.shape[:2], dtype=np.uint8)

# Set the damaged black pixel locations to white (255)
mask_gray[is_black] = 255
# Save mask
cv2.imwrite("generated_mask.jpg", mask_gray)

# Step 3: Perform inpainting (TELEA method)
restored_telea = cv2.inpaint(damaged_img, mask_gray, 3, cv2.INPAINT_TELEA)

# Save the restored image to verify it worked
cv2.imwrite("restored_telea.jpg", restored_telea)


# import cv2
# import numpy as np
# Step 4: Read damaged image again
img = cv2.imread("frog.jpg")

# Step 5: Load predefined mask (must be a binary image)
mask_predefined = cv2.imread("generated_mask.jpg", 0)

# Step 6: Inpaint with Navier-Stokes method

restored_ns = cv2.inpaint(img, mask_predefined, 3, cv2.INPAINT_NS)
# Save results
cv2.imwrite("restored_telea.png", restored_telea)
cv2.imwrite("restored_ns.png", restored_ns)

# -------------------------------
# Display Results
# -------------------------------
cv2.imshow("Original Damaged Image", damaged_img)
cv2.imshow("Generated Mask", mask_gray)
cv2.imshow("Restored (Telea)", restored_telea)
cv2.imshow("Predefined Mask", mask_predefined)
cv2.imshow("Restored (Navier-Stokes)", restored_ns)

cv2.waitKey(0)
cv2.destroyAllWindows()
