# Stereo-Vision-System

## Overview

This project demonstrates how to perform 3D reconstruction using stereo vision with OpenCV in Python. It involves detecting keypoints in two images captured from different angles, matching them, and computing the 3D coordinates of the matched points to visualize a 3D point cloud.

## Features

- **Stereo Image Processing:** Handles two images to extract depth information and reconstruct a 3D scene.
- **SIFT Keypoint Detection:** Uses Scale-Invariant Feature Transform (SIFT) to detect and describe features in both images.
- **Keypoint Matching:** Matches keypoints between the stereo images using a Brute-Force matcher with ratio test filtering.
- **3D Point Cloud Visualization:** Reconstructs and visualizes the 3D points using Matplotlib.


## Customization

- **Camera Calibration:** Adjust the intrinsic camera parameters (`K`, `fx`, `fy`, `ox`, `oy`) according to your camera's calibration.
- **Baseline Distance:** Modify the baseline (`b`) based on the actual distance between your stereo camera setup.
- **Keypoint Matching:** Tweak the ratio test threshold or experiment with different feature detectors and matchers.

## Results

### 1. Keypoint Matches Between Left and Right Images

![IMG_1](https://github.com/user-attachments/assets/7220e263-0b79-4e7b-b1e9-e314014294e3)

This image shows the matched keypoints between the left and right stereo images, with good matches highlighted.

### 2. 3D Point Cloud

![3DPoint](https://github.com/user-attachments/assets/b9bdd66d-775c-492e-b469-6e508ee59f7e)

This is the 3D point cloud generated from the matched keypoints. Each point represents a 3D coordinate reconstructed from the stereo images.

