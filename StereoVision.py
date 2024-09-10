import cv2
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

shrink=0.2
#Matrice de calibration
K = np.array([[446.11708806  , 0.        , 283.47301282],
              [  0.         ,342.43064142, 295.23805926],
              [  0.         ,  0.          , 1.        ]])
# Define the intrinsic camera matrix (already calibrated)
fx = 446.11708806
fy = 342.43064142
ox = 283.47301282
oy = 295.23805926

K = np.array([[fx, 0, ox], 
              [0, fy, oy], 
              [0, 0, 1]])

# Define the baseline (distance between the two cameras)
b = 300
# Load the left and right images (already acquired)
img_left =  cv.imread('IMG_1.JPG')
img_right = cv.imread('IMG_2.JPG')

img_left = cv2.resize(img_left, (0,0), fx=shrink, fy=shrink, interpolation=cv2.INTER_CUBIC)
img_right = cv2.resize(img_right, (0,0), fx=shrink, fy=shrink, interpolation=cv2.INTER_CUBIC)

# Detect SIFT keypoints and extract descriptors for both images
sift = cv2.SIFT_create()
kp_left, des_left = sift.detectAndCompute(img_left, None)
kp_right, des_right = sift.detectAndCompute(img_right, None)

# Match the keypoints between the two images using a Brute-Force matcher
bf = cv2.BFMatcher()
matches = bf.knnMatch(des_left, des_right, k=2)

draw_params = dict(matchColor=(0,255,0),
                       singlePointColor=None,
                       flags=2)
# Filter out the good matches using the ratio test
good_matches = []
for m, n in matches:
    if m.distance < 0.95 * n.distance:
        good_matches.append(m)
MIN_MATCH_COUNT = 80
if len(good_matches) > MIN_MATCH_COUNT:
    src_pts = np.float32([ kp_left[m.queryIdx].pt for m in good_matches ]).reshape(-1,1,2)
    dst_pts = np.float32([ kp_right[m.trainIdx].pt for m in good_matches ]).reshape(-1,1,2)
    M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)
    matchesMask = mask.ravel().tolist()
    good_matches = [m for i, m in enumerate(good_matches) if matchesMask[i]]

# Compute the 3D coordinates of the matched keypoints
points3d = []
for match in good_matches:
    ul, vl = kp_left[match.queryIdx].pt
    ur, vr = kp_right[match.trainIdx].pt
    disparity = ul - ur
    z = b * fx / disparity
    x = b *(ul-ox) / disparity
    y = b *fx*(vl-oy) / fy*disparity
    points3d.append((x, y, z))


img3 = cv2.drawMatches(img_left, kp_left, img_right, kp_right, good_matches,None,**draw_params)
cv2.imshow("Draw Matches Left Right.jpg", img3)

cv2.waitKey(0)

# Convert the list of 3D points to a numpy array
points3d = np.array(points3d)

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the points
ax.scatter(points3d[:, 0], points3d[:, 1], points3d[:, 2],c='b',marker='o')

# Set the labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend(loc='upper left')
ax.set_title('3D Point Cloud')

# Show the plot
plt.show()