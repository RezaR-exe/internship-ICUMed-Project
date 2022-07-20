import cv2
import numpy as np
import pyautogui
import time
from multiprocessing import Process, Queue
from player_youtube import youtube
from audio_recording import audio_recorder
from video_audio_merge import merge
from analyze_wav import measure_wav_db_level
import logging


# creating the logger
# if you need more detailed information about logs, you can change the level from logging.INFO to logging.DEBUG
logging.basicConfig(filename="Logs.log", level=logging.INFO)
logger = logging.getLogger()
logger.setLevel(logging.INFO)



def video_record(a):
    print(f"Recording... - {time.strftime('%H:%M:%S')}")
    logging.info(f"Recording... - {time.strftime('%H:%M:%S')}")
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
             # print(int(seconds))

         if seconds >= 120:
             video_running = False
             print(f"Video has finished recording! - {time.strftime('%H:%M:%S')}")
             print(f"Merging the final video... - {time.strftime('%H:%M:%S')}")
             logging.info(f"Video has finished recording! - {time.strftime('%H:%M:%S')}")
             logging.info(f"Merging the final video... - {time.strftime('%H:%M:%S')}")

    cv2.destroyAllWindows()
    out.release()



if __name__=="__main__":
    x=Queue()
    p1=Process(target=video_record, args=(x,))
    p2=Process(target=youtube, args=())
    p3 = Process(target=audio_recorder, args=())
    p1.start()
    p2.start()
    p3.start()
    time.sleep(130)
    print(f"Analyzing the audio... - {time.strftime('%H:%M:%S')}")
    logging.info(f"Analyzing the audio... - {time.strftime('%H:%M:%S')}")
    measure_wav_db_level("recording.wav")
    time.sleep(10)
    merge()




