import cv2
import numpy as np

# Function to preprocess image for digit extraction
def preprocess_image(img_path):
    # Read the image
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

    # Apply Gaussian blur to smooth out the image
    blur = cv2.GaussianBlur(img, (9, 9), 0)

    # Apply adaptive thresholding to get a binary image
    thresh = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
                                   cv2.THRESH_BINARY, 11, 2)

    # Invert colors so that grid lines are black and the background is white
    return cv2.bitwise_not(thresh)

# Function to find the biggest contour assuming it is the Sudoku grid
def find_biggest_contour(processed_img):
    # Find all contours
    contours, _ = cv2.findContours(processed_img.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Sort the contours by area and return the biggest
    biggest = max(contours, key=cv2.contourArea)
    return biggest

# Function to extract the corners of the biggest contour
def extract_corners_of_biggest_contour(biggest_contour, accuracy=0.02):
    peri = cv2.arcLength(biggest_contour, True)
    return cv2.approxPolyDP(biggest_contour, accuracy * peri, True)

# Preprocess the image
processed_img = preprocess_image(img_path)

# Find the biggest contour
biggest_contour = find_biggest_contour(processed_img)

# Extract the corners of the biggest contour
corners = extract_corners_of_biggest_contour(biggest_contour)

# Check if we've found a quadrilateral, which should be the Sudoku grid
if corners.shape[0] == 4:
    print("Found the corners of the Sudoku grid.")
else:
    print("Did not find a quadrilateral. Found {} points instead.".format(corners.shape[0]))

# Function to reorder points for warping
def reorder_points(pts):
    pts = pts.reshape((4, 2))
    new_pts = np.zeros((4, 2), dtype=np.float32)

    # Add the points to get the bottom-right point
    # Subtract the points to get the top-left point
    add = pts.sum(1)
    new_pts[0] = pts[np.argmin(add)]
    new_pts[2] = pts[np.argmax(add)]

    diff = np.diff(pts, axis=1)
    new_pts[1] = pts[np.argmin(diff)]
    new_pts[3] = pts[np.argmax(diff)]

    return new_pts

# Function to warp the image to a flat square
def warp_image(img, src_points):
    # Reorder points for warping
    src_points = reorder_points(src_points)
    
    # Define the size of the new image: 9x9 Sudoku grid with each cell of 28x28 pixels
    size = 9 * 28
    dst_points = np.array([[0, 0], [size - 1, 0], [size - 1, size - 1], [0, size - 1]], dtype="float32")
    
    # Get the transformation matrix
    matrix = cv2.getPerspectiveTransform(src_points, dst_points)
    
    # Apply the warp transformation
    return cv2.warpPerspective(img, matrix, (size, size))

# Warp the image to get the top-down view of the Sudoku puzzle
if corners.shape[0] == 4:
    warped_img = warp_image(processed_img, corners)
else:
    warped_img = None

# Show the processed and warped images for visualization
cv2.imshow("Processed Image", processed_img)
cv2.imshow("Warped Sudoku Grid", warped_img if warped_img is not None else np.zeros_like(processed_img))
cv2.waitKey(0)
cv2.destroyAllWindows()

# Check if the warping was successful
if warped_img is not None and warped_img.shape == (252, 252):
    print("Warping successful.")
else:
    print("Warping unsuccessful.")
