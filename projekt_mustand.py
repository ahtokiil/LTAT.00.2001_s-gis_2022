# y, sr = librosa.load(('guitar1.wav'))
# fig, ax = plt.subplots(nrows=2, ncols=1, sharex=True)
# D = librosa.amplitude_to_db(abs(librosa.stft(y)), ref=16000)
# img = librosa.display.specshow(D, y_axis='linear', x_axis='time',
#                                sr=sr, ax=ax[0])
# ax[0].set(title='Linear-frequency power spectrogram')
# ax[0].label_outer()
# plt.show()