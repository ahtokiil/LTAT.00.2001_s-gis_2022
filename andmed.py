import librosa
import librosa.display

songData, sr = librosa.load('guitar1.wav', sr = 300)				# sr = sample rate, mis määrab suuruse, mitu korda sekundis audio väljundit esitatakse;
                                                                    # antud juhul tähendab see helifailis toimuvate kohta andmete kogumist ühes sekundis.
                                                                    # sr = 10 annab 30 sek loo korral 300 kannet järjendisse songData

andmed1 = []
for el in songData:
    andmed1.append((round(float(el)*10**3),2))


tempoData, sr = librosa.load('guitar1.wav', sr = 14400)				# sr peab olema suurem, sest väga väikese väärtusega tuleb üksluisete väärtuste kogum.
tempo, lööke = librosa.beat.beat_track(y = tempoData, sr = sr)


hop_length = 512
oenv = librosa.onset.onset_strength(y = tempoData, sr = 14400, hop_length = hop_length)
tempogram = librosa.feature.tempogram(onset_envelope = oenv, sr = 14400,
                                      hop_length=hop_length)

                                                                    # Kogume andmed pala tempomuutuste kohta, et saada +/- väärtusi värviskaalal liikumiseks.
andmed2 = []
for tmp in range(len(tempoData)-1):
    andmed2.append(int(tempoData[tmp]/tempoData[tmp+1]))