import cv2
import numpy as np
import pyautogui
import time


def screen_recorder():
    # set the screen resolution for the recorder
    screen_size = (1920, 1080)

    # create the recording codec
    fourcc = cv2.VideoWriter_fourcc(*"XVID")

    # set the output file of the recording
    out = cv2.VideoWriter("output.avi", fourcc, 20.0, (screen_size))
    # set the frames per second
    fps = 60
    # this is for slowing down the video processing
    prev = 0
    # a boolean for the loop
    video_running = True
    # setting an integer for the seconds
    seconds = 0


    while video_running:

        # this calculates the time elapsed since starting the recording
         time_elapsed = time.time() - prev
        # this takes a screenshot per every frame
         img = pyautogui.screenshot()
         if time_elapsed > 1.0/fps:
             # this updates the time
             prev = time.time()
             # this adds the frame taken to an numpy array
             frame = np.array(img)
             # this changes the color of the frame from BGR (blue, green, red) to RGB (red, green, blue)
             frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
             # this writes the converted frame to the output file
             out.write(frame)
             # this adds seconds to the second counter
             seconds += 0.05
             # this prints the second every time it is updated
             print(seconds)

        # an if statement for breaking the loop after the selected seconds, you can edit the seconds below
         if seconds >= 20:
             video_running = False


    # this closes all opened windows and releases the final recorded file
    cv2.destroyAllWindows()
    out.release()

# uncomment this to call the function
# screen_recorder()





