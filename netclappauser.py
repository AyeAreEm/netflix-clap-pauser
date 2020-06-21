from pynput.keyboard import Key, Controller
import sounddevice as sd
import numpy as np

thresh = 0

keyboard = Controller()

def print_sound(indata, outdata, frames, time, status):
    global thresh
    volume_norm = np.linalg.norm(indata) * 10
    currentVol = (int(volume_norm))
    print(currentVol)

    if currentVol > thresh:
        thresh = thresh + 4
        print("True")
        print(str(thresh))
        keyboard.press(Key.space)
        keyboard.release(Key.space)

with sd.Stream(callback = print_sound):
    sd.sleep(100000)
