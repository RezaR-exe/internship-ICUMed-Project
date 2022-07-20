# this code is for merging one audio file ino a video file
import subprocess
import time
import logging

# creating the logger
# if you need more detailed information about logs, you can change the level from logging.INFO to logging.DEBUG

logging.basicConfig(filename="Logs.log", level=logging.INFO)
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def merge():
    try:
        # instantiating the command
        # this command merges the audio and video file into one mp4 file using ffmpeg
        cmd = r'ffmpeg -y -i recording.wav  -r 30 -i output.avi  -filter:a aresample=async=1 -strict -2 -c:a flac -c:v copy video_with_sound.mp4 2> ffmpegoutput.txt -y'
        # calling the command line and pasting the command above
        subprocess.call(cmd, shell=True)                                     # "Muxing Done
        print(f"Merging the audio and video has finished succesfully! - {time.strftime('%H:%M:%S')}")
        logging.info(f"Merging the audio and video has finished succesfully! - {time.strftime('%H:%M:%S')}")
    except:
        print(f"The audio or video file has been corrupted or was not found - {time.strftime('%H:%M:%S')}")
        logging.info(f"The audio or video file has been corrupted or was not found - {time.strftime('%H:%M:%S')}")


