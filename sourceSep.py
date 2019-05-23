"""
Name:           Carlos Meza
Description:
  Using ICA and PCA, seperate two signals(voice and siren) into seperate files and output both into wav files.
"""


import numpy as np
import soundfile as sf
from scipy import signal
from sklearn.decomposition import FastICA, PCA

def unmixAudio(leftName, rightName) :
        # Read in both files, left and right with samplerates
        left, l_rate = sf.read(leftName)
        right, r_rate = sf.read(rightName)
        # Create a mixed array of both signals into one matrix
        S = np.c_[left, right]
        # Compute ICA
        ica = FastICA(n_components=2)
        # Reconstruct SIgnals
        S1 = ica.fit_transform(S)
        # Multiply by 10 to increase output values
        S1 = np.multiply(S1, 10)
        # Output both files to wav file by each column seperately
        sf.write('unmixed0.wav', S1[:,0], l_rate)
        sf.write('unmixed1.wav', S1[:,1], r_rate)

###################  main  ###################
if __name__ == "__main__" :
    leftName = "darinSiren0.wav"
    rightName = "darinSiren1.wav"
    unmixAudio(leftName, rightName)
