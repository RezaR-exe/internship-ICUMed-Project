import cv2
import numpy as np
import pyautogui
import time


def screen_recorder():
    screen_size = (1920, 1080)

    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    out = cv2.VideoWriter("output.avi", fourcc, 20.0, (screen_size))

    fps = 60
    prev = 0
    video_running = True
    seconds = 0


    while video_running:
         time_elapsed = time.time() - prev
         img = pyautogui.screenshot()
         if time_elapsed > 1.0/fps:
             prev = time.time()
             frame = np.array(img)
             frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
             out.write(frame)
             seconds += 0.05
             print(seconds)

         if seconds >= 20:
             video_running = False



    cv2.destroyAllWindows()
    out.release()


screen_recorder()


































# alternative script
# screen_size = (1920, 1080)
#
#
# fourcc = cv2.VideoWriter_fourcc(*"XVID")
# out = cv2.VideoWriter("output.avi", fourcc, 20.0, (screen_size))
#
# fps = 60
# prev = 0
# video_running = True
# secs = 0
#
# while video_running:
#      time_elapsed = time.time() - prev
#      img = pyautogui.screenshot()
#      if time_elapsed > 1.0/fps:
#          prev = time.time()
#          frame = np.array(img)
#          frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#          out.write(frame)
#          secs += 0.01
#      if secs >= 24:
#          video_running = False
#
#
# cv2.destroyAllWindows()
# out.release()












# alternative script
# screen_size = tuple(pyautogui.size())
#
#
# fourcc = cv2.VideoWriter_fourcc(*"XVID")
#
# fps = 30
#
# out = cv2.VideoWriter("output.avi", fourcc, fps, (screen_size))
#
#
# record_seconds = 120
#
# for i in range(int(record_seconds * fps)):
#     img = pyautogui.screenshot()
#     frame = np.array(img)
#     frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#     out.write(frame)
#     # cv2.imshow("screenshot", frame)
#
#     if cv2.waitKey(1) == ord("q"):
#         break
#
# cv2.destroyAllWindows()
# out.release()






