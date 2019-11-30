 
import pydub
import os
import librosa
import matplotlib.pyplot as plt

from fastai import *
from fastai.vision import *


cmap = plt.get_cmap('inferno')
plt.figure(figsize=(10,10))


def predictor(song):
    img = song_to_img(song)
    model = load_learner('models/')
    return model.predict(img)


def song_to_img(song):
    if song.endswith('.mp3'):
        sound = pydub.AudioSegment.from_mp3(f'songs/{song}')
        song = song[:-4] + '.wav'
        sound.export(f'songs/{song}', format="wav")
    offset = 0 if 0 > librosa.get_duration(filename=f'songs/{song}')/2 - 15 else librosa.get_duration(filename=f'songs/{song}')/2 - 15
    y, sr = librosa.load(f'songs/{song}', mono=True, duration=30, offset=offset)
    plt.specgram(y, NFFT=2048, Fs=2, Fc=0, noverlap=128, cmap=cmap, sides='default', mode='default', scale='dB')
    plt.axis('off')
    plt.savefig(f'static/images/{song[:-4]}.png', transparent=True)
    return open_image(f'static/images/{song[:-4]}.png')
    
