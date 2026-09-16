import cv2
import numpy as np


def detect_object(template_path, input_image_path):

    # Read the template image in grayscale
    template = cv2.imread(template_path, 0)

    if template is None:
        raise FileNotFoundError(
            "Template image not found. Check the template path."
        )

    # Read the input image
    img = cv2.imread(input_image_path)

    if img is None:
        raise FileNotFoundError(
            "Input image not found. Check the input image path."
        )

    # Convert the input image to grayscale
    gray_img = cv2.cvtColor(
        img,
        cv2.COLOR_BGR2GRAY
    )

    # Get the width and height of the template image
    w, h = template.shape[::-1]

    # Perform template matching
    res = cv2.matchTemplate(
        gray_img,
        template,
        cv2.TM_CCOEFF_NORMED
    )

    # Set a threshold for matching
    threshold = 0.8

    # Find locations where the match is above the threshold
    loc = np.where(res >= threshold)

    # Draw rectangles around matched areas
    for pt in zip(*loc[::-1]):

        cv2.rectangle(
            img,
            pt,
            (pt[0] + w, pt[1] + h),
            (0, 255, 255),
            2
        )

    # Display the input image with detected objects
    cv2.imshow(
        "Detected Objects",
        img
    )

    cv2.waitKey(0)
    cv2.destroyAllWindows()


# --------------------------------
# Provide image paths
# --------------------------------

template_path = "images.jfif"

input_image_path = "images.jfif"


# --------------------------------
# Detect the object
# --------------------------------

detect_object(
    template_path,
    input_image_path
)