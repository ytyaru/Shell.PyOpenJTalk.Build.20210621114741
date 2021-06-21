import pyopenjtalk
import numpy
import simpleaudio as sa
x, sr = pyopenjtalk.tts('なにか喋ります。', volume=1.0, weight=9.0)
ply = sa.play_buffer(x.astype(numpy.int16), 1, 2, sr)
ply.wait_done()
