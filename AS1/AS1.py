import tkinter as tk
import os, os.path
window = tk.Tk()
import wave
import matplotlib.pyplot as plt 
import numpy as np 

with wave.open("test samples/Q1/audio1.wav", 'r') as wav_file:
   print(wav_file.getnframes())
   data = wav_file.readframes(-1)
   data = np.frombuffer(data, dtype ="int16") 

   print(data)

with wave.open("test samples/Q1/audio2.wav", 'r') as wav_file2:
   print(wav_file2.getnframes())
   data2 = wav_file2.readframes(-1)
   data2 = np.frombuffer(data2, dtype ="int16") 

   print(data2)

entry = tk.Button(text="Open File")
print(os.listdir("test samples/Q1"))
print(wav_file.getnchannels())
print(wav_file2.getnchannels())
# button.pack(pady=50)
entry.pack()
window.mainloop()
