# Sentry
Sentry is a smart security camera built using Python and OpenCV. It uses real-time face recognition to identify family members. Face detection is done using the 
Haar Cascades object detection algorithm, and face recognition through the LBPH algortihm both of which are available to implement in OpenCV.

# Prerequisites
Python, pip, virtualenv, and the latest version of OpenCV are required to run this project. Once python is installed, install pip using the command ```sudo apt install python3-pip``` for linux, and ```py -m ensurepip --upgrade``` for windows. Once pip is installed, install virtualenv by running the command ```pip install virtualenv```.
To set up a virtual environment, open up the terminal, navigate to the directory where you want to create the virtual environment and run the command ```python3 -m venv .``` for linux, and ```python -m venv .``` for windows.
After the virtual envionment is set up, you need to activate it. Navigate to the directory where you have created the venv, and run the command ```Scripts\activate``` for Windows, and ```source activate``` for linux systems.
Once activated, run ```pip install requirements.txt``` to install the necessary packages to run the program.

# Methodology
This project consists of three main stages: Data Collection, Model Training, and Recognition.

## Data collection
In this stage the face data of all the people who you want to recognize is captured and stored in a directory called 'datasets'. This stage uses the Haar Cascades object detection algorithm to detect faces. Haar Cascades is an algorithm for object detection which was proposed back in 2001, which uses Haar features and a boosted cascade to detect objects. Its implementation is readily available in OpenCV.
## Model Training
In this stage the face data is fed to the LBPH algorithm, that is trained to recognize the faces in the given dataset. LBPH or Local Binary Pattern Histogram, is an algorithm for recognizing faces. In the first step, Local binary patterns are generated from the image to accentuate the characteristcs of the image. The image is then divided into a grid and the histogram of each grid is concatenated which is it. 
For recognition, the same process is applied to the freash face and the two histograms are compared to give the prediction. The lesser the confidence, the stronger the prediction.
## Recognition 
In the final stage, a fresh set of faces is given to the recognizer in the form of a video feed and it returns the id along with the confidence of it's prediction.

# Running the program
Now that we have gone through its implementation, we can run the program. To do so, open up the terminal, activate your venv, and run the command ```python startup.py```
following which, you will be prompted with the UI 

Go through the general instructions to set up sentry and once done you are all ready to go!.

Here is a working example. In this example I have gone through the set up stages.

![demo]()



