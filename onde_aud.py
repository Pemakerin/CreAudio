import numpy as np
import soundfile as sf

# Vamos apernas criar uma onde simple
# com a frenquencia 44100 que sera a quantidade
# de amotras que a biblioteca vai calcular, 
# depois salvamos ele em um arquivo com
# tipo de formatação em WAV

time = 1.0 # Tempo em segundos 
fq = 440 # frequencia de amotras 44100

# Gerar tempo de amostras entre 0 e 1 segundos ou mas conformer a variavel time
samples = np.arange(44100 * time) / 44100.0

# Lembre-se de que uma onda senoidal de frequência f tem a fórmula w(t) = A*sin(2*pi*f*t)
wave = 1000000 * np.sin(2 * np.pi * fq * samples)

# Convertendo para formato wav (16 bits)
wav_wave = np.array(wave, dtype=np.int16)

# salvando em um arquivo como "som_null.wav" com formatação WAV
sf.write("som_null.wav", wav_wave, 44100)
