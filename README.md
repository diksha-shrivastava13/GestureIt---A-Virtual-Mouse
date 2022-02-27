# GestureIt---A-Virtual-Mouse
GestureIt is a virtual mouse, which receives gesture-based input from users and can perform the basic mouse functions of moving, single left click, scrolling upwards and downwards and right click functions in response to gestures.  


##### **Introduction/Background:**
A gesture-based system eliminates the need of physical touch with devices, making large settings with public devices, such as computer labs, safer for public use. It also improves user experience by greatly increase the ease of communication with devices, without having a perform a huge number of tasks in between. Most importantly, a gesture-based system would be of huge help to anyone with speaking disabilities. 
##### **Objectives:**  
Objective is to build a program that can perform all basic mouse functions with hand-based gestures as input.
##### **Methods:**
Using OpenCV to access camera feed, read and show frames, Mediapipe is used to detect and track hand landmarks. The coordinates of these hand landmarks are used to determine whether fingers are up or not. Conditions are set to perform mouse functions using AutoPy and PyAutoGUI depending on which fingers are up and what is the distance between them.
##### **Keywords:**
Machine Learning, Computer Vision

## Why GestureIt?
**Eliminating the Need of Physical Interaction:** Every interaction with gadgets, thus far, is based either on touch (mouse, keyboard etc.) or on voice (intelligent personal assistants like Alexa, Siri, Cortana, Google Assistant). In times of Covid-19, it isn’t safe for people to physically interact with devices, especially in large public settings like cyber cafes, computer laboratories etc. A gesture-based interface eliminates the need of physically interacting with devices, thus rendering the aforementioned settings safe for public use.

**Enhancing User Experience:** A gesture-based user interface is the first step towards the day when you can simply throw up a peace sign from across the room to start playing your favorite game or a thumbs-up sign on which your desktop starts playing your favorite music. In the current state, for the above, you’d need to cross the room, start your device, search for the music app, search for your favorite music and only then you can hear it. When dealing with mobile phones, you’d still have to search for your phone, draw a gesture or search for the app and then music. A gesture-based system eliminates all these unnecessary steps in between, you just have to make a peace sign with your fingers. It makes technology come alive around you, thus greatly enhancing the user experience.

**Metaphorical Staff for Everyone with Speaking Disabilities:** Those without any speaking disabilities or loss of control over limbs enjoy the ease of living with voice-based personal assistants, which is something that the disabled among us are missing out on. With a gesture-based interface, their ease of access will greatly be increased when they can simply use sign language to input commands. 


#### The method followed:
Create an object to access camera feed with OpenCV. Read frames, if frames are read correctly, use Mediapipe to detect hands and hand landmarks and use Mediapipe’s drawing utils to draw the hand landmarks.
After this, the task is to check which fingers are up by comparing the coordinates of [4, 8, 12, 16, 20], each corresponding to tip of a finger, with another finger’s coordinates. 
If the said finger is up, append value 1 in the fingers list corresponding to the index of the finger, if not append 0.
For example, if every finger except the thumb and the index finger is down, then the resultant fingers list would be [1, 1, 0, 0, 0].
Now, as we can figure out which fingers are up and which are down in real time, we simply have to set conditions for mouse functions according to the gestures.

#### The Five Mouse Functions and Gestures:
1.	**The Moving Mode:** If only the index finger is up, i.e. fingers[1] == 1, then the mouse is in moving mode. To move the mouse, use autopy’s mouse.smooth_move() function, with coordinates of the tip of moving finger in the reduced frame as parameters.
2.	**The Single Left Click:** If both middle and index fingers are up and the distance between them is less than a minimum value, a single left click should happen. For this, use autopy’s mouse.click() function.
3.	**The Downward Scroll:** If the thumb and the index fingers are brought together, then the downward scroll should take place corresponding to the number of clicks passed as negative parameters in pyautogui.scroll() function.
4.	**The Upward Scroll:** If the little finger and the index finger are brought together, then the upward scroll should take place corresponding to the number of clicks passed as positive parameters in pyautogui.scroll() function.
5.	**The Right Click:** If the three middle fingers are brought together, then a right click should happen using pyautogui.click(button=”right”) function.


**To run the project:**

First clone the repository with: git clone https://github.com/diksha-shrivastava13/GestureIt---A-Virtual-Mouse.git

Intsall the requirements: pip install -r requirements.txt

Run the automouse.py module with parameter of cv2.VideoCapture() set to the index of your camera. 

You're now ready to switch to a gesture-based mouse!

