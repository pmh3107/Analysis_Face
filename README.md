# Analysis_Face

Welcome to Analysis_Face! This is a project focusing on facial analysis using various techniques and libraries.

## Overview

This project aims to provide facial analysis capabilities, including age estimation, gender recognition, race detection, and emotion recognition. It utilizes deep learning models and computer vision algorithms to analyze facial attributes from images or live video streams.

## Features

1. Accurate facial analysis:

- Age estimation: Predicts the age of individuals in the image or video.
- Gender recognition: Determines the gender (male/female) of individuals in the image or video.
- Race detection: Identifies the race or ethnicity of individuals in the image or video.
- Emotion recognition: Recognizes the primary emotion (e.g., happy, sad, angry) displayed by individuals in the image or video.

2. Real-time facial analysis:

- Guess age: Predicts the age of individuals in video of camera.
- Guess gender: Determines the gender (male/female) in video of camera.

## Installation

To run this code, please ensure you have the following dependencies installed:

- numpy>=1.14.0
- pandas>=0.23.4
- gdown>=3.10.1
- tqdm>=4.30.0
- Pillow>=5.2.0
- opencv-python>=4.5.5.64
- tensorflow>=1.9.0
- keras>=2.2.0
- Flask>=1.1.2
- mtcnn>=0.1.0
- retina-face>=0.0.1
- fire>=0.4.0
- gunicorn>=20.1.0

You can install these dependencies using pip: `pip install -r requirements.txt`

Make sure to replace `requirements.txt` with the actual name of your requirements file, if different.

## How to Run

1. Make sure you have Python installed on your computer. If not, you can download Python from the [official Python website](https://www.python.org/downloads/) and follow the instructions to install it.

2. Download the source code from this repository to your computer.

3. Open a terminal or command prompt, then navigate to the directory containing the downloaded source code.

4. Run the application by entering the following command:

   ```
   python main.py
   ```

5. After running the above command, a graphical user interface window will appear, allowing you to interact with the features of the "ANALYSIS FACE" application.

## Usage

After installing the dependencies, you can run the project by executing the main script or launching the appropriate application. Follow the instructions provided in the project documentation for more details on usage and functionality.

## Theme of the Project

![PrimaryTheme](https://firebasestorage.googleapis.com/v0/b/mycv-3107.appspot.com/o/Project_Analysis_Face%2FTheme_main.png?alt=media&token=a6133dbd-e718-426b-ad65-56912c4c3086)

## How I made it ...

## Explanation of **main**() Function

The `__main__()` function in the code is responsible for setting up the main graphical user interface (GUI) window of the "ANALYSIS FACE" application. Below is a breakdown of its components and functionalities:

1. **Importing Required Libraries:**

   - The function begins by importing necessary libraries such as `Path` from `pathlib` for file path manipulation and various modules from `tkinter` for creating GUI elements.

2. **Defining the `destroy_window()` Function:**

   - This function is a helper function that takes a window parameter and destroys the window when called. It is used to close the application window.

3. **Defining the `main()` Function:**

   - Inside the `main()` function, paths to assets like images are defined using `Path`.
   - A Tkinter window is created with the title "ANALYSIS FACE" and dimensions 900x600.
   - A Canvas widget is placed inside the window with a white background to contain other GUI elements.
   - Buttons are placed on the canvas using `Button` widget, each associated with a specific image and command to execute a particular function when clicked.
   - Rectangles and text elements are drawn on the canvas to provide visual presentation.
   - Images are imported and displayed on the canvas.
   - Window properties such as resizable are configured, and the GUI main loop is started.

4. **Running the Application:**
   - Finally, the script checks if it's being run directly using `if __name__ == "__main__":` and calls the `main()` function to start the application.

This code sets up the primary user interface of the "ANALYSIS FACE" application, allowing users to interact with various features related to face analysis.

## Explanation of `show_user_manual()` Function

The `show_user_manual()` function is responsible for displaying the user manual interface in the "ANALYSIS FACE" application. Here's a breakdown of its components and functionalities:

1. **Importing Required Libraries:**

   - The function imports necessary libraries such as `Path` from `pathlib` for file path manipulation and various modules from `tkinter` for creating GUI elements.

2. **Defining the `back_to_main()` Function:**

   - This function takes two parameters: `back_to_main_screen` and `window`. It destroys the current window and calls the `back_to_main_screen()` function to return to the main screen.

3. **Setting Up User Manual Interface:**

   - Inside the `show_user_manual()` function, paths to assets like images are defined using `Path`.
   - A Canvas widget is created inside the window with a white background to contain other GUI elements.
   - Rectangles and text elements are drawn on the canvas to provide visual presentation of the user manual.
   - An image is imported and displayed on the canvas for illustration purposes.
   - Text is added to describe the usage options of the application, including options for accurate facial analysis and real-time facial analysis.

4. **Adding a Button to Return to Main Screen:**

   - A button is placed on the canvas to allow users to return to the main screen when clicked. The button is associated with the `back_to_main()` function.

5. **Configuring Window Properties and Starting GUI Main Loop:**
   - Window properties such as resizable are configured, and the GUI main loop is started to display the user manual interface.

This function enhances the user experience by providing clear instructions and usage options for the "ANALYSIS FACE" application.

## Explanation of `predict_age_gender()` Function

The `predict_age_gender()` function is responsible for displaying the interface to predict age and gender using the camera feed in the "ANALYSIS FACE" application. Here's a breakdown of its components and functionalities:

1. **Importing Required Libraries:**

   - The function imports necessary libraries such as `Tk`, `Canvas`, `Button`, `PhotoImage` from `tkinter` for creating GUI elements and `Path` from `pathlib`.

2. **Defining the `back_to_main()` Function:**

   - This function takes two parameters: `back_to_main_screen` and `window`. It destroys the current window and calls the `back_to_main_screen()` function to return to the main screen.

3. **Setting Up Prediction Interface:**

   - Inside the `predict_age_gender()` function, paths to assets like images are defined using `Path`.
   - A Canvas widget is created inside the window with a white background to contain other GUI elements.
   - A rectangle is drawn on the canvas for the header with text "Analyze Face" for visual presentation.
   - A button is placed on the canvas to allow users to return to the main screen when clicked. The button is associated with the `back_to_main()` function.

4. **Creating Video Canvas:**

   - Another Canvas widget is created to display the camera feed for real-time face analysis.
   - This canvas is positioned at a specific location on the window.
   - The `recognize_age_gender_camera()` function is called to start capturing the camera feed and perform real-time age and gender prediction.

5. **Configuring Window Properties and Starting GUI Main Loop:**
   - Window properties such as resizable are configured, and the GUI main loop is started to display the prediction interface and camera feed.

This function enhances the user experience by providing real-time age and gender prediction using the camera feed in the "ANALYSIS FACE" application.

## Explanation of `analyze_face_accurate()` Function

The `analyze_face_accurate()` function is responsible for displaying the interface to analyze faces accurately in the "ANALYSIS FACE" application. Here's a breakdown of its components and functionalities:

1. **Importing Required Libraries:**

   - The function imports necessary libraries such as `Canvas`, `Button`, `PhotoImage` from `tkinter` for creating GUI elements and `Path` from `pathlib`.

2. **Defining the `back_to_main()` Function:**

   - This function takes two parameters: `back_to_main_screen` and `window`. It destroys the current window and calls the `back_to_main_screen()` function to return to the main screen.

3. **Setting Up Face Analysis Interface:**

   - Inside the `analyze_face_accurate()` function, paths to assets like images are defined using `Path`.
   - A Canvas widget is created inside the window with a white background to contain other GUI elements.
   - A rectangle is drawn on the canvas for the header with text "Analyze Face" for visual presentation.
   - Another Canvas widget (`canvas_video`) is created to display the video feed for face analysis. It is positioned at a specific location on the window.
   - Text information is displayed on the canvas to provide feedback or instructions during face analysis.

4. **Creating Buttons for Interaction:**

   - Buttons are placed on the canvas to allow users to interact with the application.
   - Each button is associated with a specific function to perform different actions:
     - The first button allows users to return to the main screen when clicked.
     - The second button triggers the function `capture_face()` to capture and analyze faces from the video feed.
     - The third button triggers the function `capture_and_analyze_face_from_file()` to capture and analyze faces from a file.
   - The buttons are positioned at specific locations on the canvas for better usability.

5. **Configuring Window Properties and Starting GUI Main Loop:**
   - Window properties such as resizable are configured, and the GUI main loop is started to display the face analysis interface and video feed.

This function provides users with the ability to analyze faces accurately using the camera feed or image files in the "ANALYSIS FACE" application.

## Explanation of Face Detection and Recognition Functions

This code contains functions for face detection and recognition using OpenCV in Python. Here's a breakdown of its components and functionalities:

1. **`faceBox(faceNet, frame)` Function:**

   - This function takes the pre-trained face detection model (`faceNet`) and a frame from a video feed (`frame`) as input.
   - It detects faces in the input frame using the face detection model and returns the frame with bounding boxes drawn around detected faces (`frame`) and a list of bounding box coordinates (`bboxs`).
   - The confidence threshold for face detection is set to 0.7.

2. **`recognize_age_gender_camera(canvas)` Function:**

   - This function performs real-time face recognition and age-gender estimation using a camera feed.
   - It initializes pre-trained models for face detection, age estimation, and gender estimation using the paths specified in the function.
   - The face detection model is used to detect faces in each frame of the camera feed.
   - For each detected face, the function extracts the face region, performs age and gender estimation using the corresponding models, and draws the predicted age and gender labels on the frame.
   - The processed frame is then converted to an image compatible with Tkinter and displayed on the provided canvas for real-time visualization.
   - The function continues to process frames from the camera feed until the user presses the 'q' key to quit.

3. **Main Loop and Cleanup:**
   - The function starts capturing video from the default camera using `cv2.VideoCapture(0)`.
   - It processes each frame by calling the `faceBox()` function to detect faces and `recognize_age_gender_camera()` function to perform age-gender estimation.
   - The processed frame is displayed on the provided canvas using Tkinter.
   - The main loop continues until the user presses the 'q' key, upon which the video capture is released and OpenCV windows are destroyed.

This code provides a simple yet effective solution for real-time face detection, age estimation, and gender estimation using OpenCV in Python.

## Face Analysis and Recognition Functions

This code contains functions for analyzing and recognizing faces using DeepFace and OpenCV in Python. Below is an explanation of each function:

1. **`show_info_message(message)` Function:**

   - This function displays an information message box with the provided message.

2. **`resize_and_save_image(img_path, canvas)` Function:**

   - This function resizes the input image if its dimensions exceed the dimensions of the canvas.
   - It saves the resized image to a new file and returns the path to the resized image.

3. **`frame_face(frame, age, gender, race, emotion)` Function:**

   - This function draws bounding boxes and labels for age, gender, race, and emotion on each detected face in the input frame.
   - It returns the modified frame with annotations.

4. **`analyze_face(img_path, canvas, original_img=None)` Function:**

   - This function analyzes the face in the provided image using DeepFace.
   - It extracts age, gender, race, and emotion information from the analyzed face and displays it on the canvas.
   - If `original_img` is provided, it draws the face annotations on the original image and displays it on the canvas.

5. **`capture_and_analyze_face_from_file(canvas)` Function:**

   - This function allows the user to select an image file from their system.
   - It analyzes the selected image for faces and displays the original image with face annotations on the canvas.

6. **`capture_face(canvas, window)` Function:**
   - This function captures a face from the webcam feed.
   - It saves the captured face as an image file and analyzes it for age, gender, race, and emotion, displaying the annotated face on the canvas.

These functions provide a comprehensive solution for face analysis and recognition tasks using DeepFace and OpenCV in Python.

## Contribution

Contributions are welcome! If you have any ideas for improvement, new features to add, or bug fixes, feel free to open an issue or submit a pull request.
