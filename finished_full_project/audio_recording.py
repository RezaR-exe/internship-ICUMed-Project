import sounddevice as sd
import time
from scipy.io import wavfile
import logging


# creating the logger
# if you need more detailed information about logs, you can change the level from logging.INFO to logging.DEBUG
logging.basicConfig(filename="Logs.log", level=logging.INFO)
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# uncomment this to get a list of your input/output devices
# print(sd.query_devices())


def audio_recorder():
    print(f"Audio Recording... - {time.strftime('%H:%M:%S')}")
    logger.info(f"Audio Recording... - {time.strftime('%H:%M:%S')}")
    # selecting which device to record
    sd.default.device[0] = 1
    # setting the frequency
    fs = 44100  # Hz
    # setting the length for which the audio may record
    length = 120  # s
    # starting recording
    recording = sd.rec(frames=fs * length, samplerate=fs, blocking=True, channels=1)
    # waiting for each frame
    sd.wait()
    # exporting the final recording into a wav audio file
    wavfile.write("recording.wav", fs, recording)
    print(f"Audio has finished Recording! - {time.strftime('%H:%M:%S')}")
    logger.info(f"Audio has finished Recording! - {time.strftime('%H:%M:%S')}")

