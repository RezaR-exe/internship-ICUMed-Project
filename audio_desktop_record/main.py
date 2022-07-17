import sounddevice as sd

# uncomment this if you want a list of your input/output devices
# print(sd.query_devices())



def audio_recorder():

    # select which device to record
    sd.default.device[0] = 1
    # set the Hz
    fs = 44100  # Hz
    # Set the length of the recording
    length = 120  # s
    # Start recording
    recording = sd.rec(frames=fs * length, samplerate=fs, blocking=True, channels=1)
    # wait for each frame
    sd.wait()
    # import the file manager that is used to save the recording to a wav file
    from scipy.io import wavfile
    # finally, save the recorded sound to a wav file
    wavfile.write('output.wav', fs, recording)
