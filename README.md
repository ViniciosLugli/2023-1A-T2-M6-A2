# 2023 - Módulo 6 - Avaliação 2

### Face Detection in Video using OpenCV

This code demonstrates how to perform face detection in a video using OpenCV library in Python. It utilizes the Haar Cascade classifier to detect faces in each frame of the input video and marks rectangles around the detected faces. The modified frames are then displayed in real-time and saved into an output video.

## Introduction

The code uses OpenCV's Haar Cascade classifier to detect faces in a video stream. It draws rectangles around the detected faces and saves the modified frames into a new video file.

# Running

## Requirements

To run the code, you need to install the required Python packages. You can install them using the following command:

```bash
pip install -r requirements.txt
```

## Usage

In the root folder, run the following command:

```bash
python src/face_detection.py
```

Now you can see the modified frames in real-time and the output video will be saved in the "output" folder.

## Output

The code saves the modified frames with rectangles around the detected faces in a new video file. The output video is saved in the "output" folder as "output_demo.mp4".

[output_demo.webm](https://github.com/ViniciosLugli/2023-1A-T2-M6-A2/assets/40807526/19748554-179b-4001-a6af-c5ff83820a6c)

# Notes

The Haar Cascade classifier used for face detection is loaded from the pre-trained XML file 'haarcascade_frontalface_default.xml'. Make sure the XML file is present in the environment before running the code ( normally is included in the OpenCV package, but you can download it from [here](https://github.com/opencv/opencv/tree/master/data/haarcascades).
The used classifier is trained to detect faces in the frontal view. It may not detect faces in other views, making it less accurate...

# Main references

-   https://docs.opencv.org/3.4/db/d28/tutorial_cascade_classifier.html
-   https://docs.opencv.org/3.4/d1/de5/classcv_1_1CascadeClassifier.html
-   https://docs.opencv.org/3.4/dd/d9e/classcv_1_1VideoWriter.html
