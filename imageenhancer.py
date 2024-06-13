import cv2
import numpy as np


def sharpness(img):
    kernel = np.array([[0, -0.5, 0],
                       [-0.5, 3, -0.5],
                       [0, -0.5, 0]])
    return cv2.filter2D(img, -1, kernel)


def bw(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


# read image and insert path
image = cv2.imread("/Users/jayanshrestha/Downloads/Jammy's/abc.png")

# changes
sharp_image = sharpness(image)
bw_image = bw(image)

# input
try:
    user_input = int(input("Press 1 to sharpen, 2 to turn it to bw or 3 to do both? : "))

    if user_input == 1:
        user_input = sharp_image
    elif user_input == 2:
        user_input = bw_image
    elif user_input == 3:
        user_input = sharpness(bw_image)
    else:
        print("Error!")

# save image
    cv2.imwrite("improved.png", user_input)
    print("Image Saved Successfully")

except Exception as e:
    print(f"Image failed to save {e}")
