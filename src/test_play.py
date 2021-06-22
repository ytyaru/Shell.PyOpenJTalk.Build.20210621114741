#!/usr/bin/env python3
# coding: utf8
import pyopenjtalk
import numpy
import simpleaudio as sa

x, sr = pyopenjtalk.tts('なにか喋ります。')
#x, sr = pyopenjtalk.tts('なにか喋ります。', weight_f0=0.9)
#x, sr = pyopenjtalk.tts('なにか喋ります。', weight=0.15)
#x, sr = pyopenjtalk.tts('なにか喋ります。', all_pass=0.35, weight=0.4)
#x, sr = pyopenjtalk.tts('ファイルに保存します。', riff_file_name='/tmp/work/test.wav')

# 肝心の音声がファイルに出力されない。中身が空っぽだった。riffでwaveファイルに保存するらしいのだが本当にriff部分しか保存されてない。
#x, sr = pyopenjtalk.tts('ファイルに保存します。', file_name='/tmp/work/test.wav')
#x, sr = pyopenjtalk.tts('ファイルに保存します。', riff_file_name='/tmp/work/test.wav')
#x, sr = pyopenjtalk.tts('ファイルに保存します。', label_file_name='/tmp/work/test.wav')
#x, sr = pyopenjtalk.tts('ファイルに保存します。', param_file_name='/tmp/work/test.wav')
"""
x, sr = pyopenjtalk.tts('なにか喋ります。')
x, sr = pyopenjtalk.tts('なにか喋ります。', speed=3.0)
x, sr = pyopenjtalk.tts('なにか喋ります。', half_tone=0.2)
x, sr = pyopenjtalk.tts('なにか喋ります。', sampling_frequency=48000*2)
x, sr = pyopenjtalk.tts('なにか喋ります。', frame_period=10)
x, sr = pyopenjtalk.tts('なにか喋ります。', all_pass=0.2)
x, sr = pyopenjtalk.tts('なにか喋ります。', postfiltering=0.2)
x, sr = pyopenjtalk.tts('なにか喋ります。', threshold=0.2)
x, sr = pyopenjtalk.tts('なにか喋ります。', weight=0.2)
x, sr = pyopenjtalk.tts('なにか喋ります。', weight_f0=0.2)
x, sr = pyopenjtalk.tts('なにか喋ります。', volume=0.2)
x, sr = pyopenjtalk.tts('なにか喋ります。', buffer_size=1024)
x, sr = pyopenjtalk.tts('なにか喋ります。', file_name='/tmp/work/test.wav')
x, sr = pyopenjtalk.tts('なにか喋ります。', info_file_name='/tmp/work/test_info.txt')
x, sr = pyopenjtalk.tts('なにか喋ります。', label_file_name='/tmp/work/test_label.txt')
x, sr = pyopenjtalk.tts('なにか喋ります。', riff_file_name='/tmp/work/test_riff.txt')
"""

ply = sa.play_buffer(x.astype(numpy.int16), 1, 2, sr)
ply.wait_done()

# 
# htsvoiceファイルを変更する。
# 
import os.path
text = 'この文章をしゃべります。'
#voice = '/home/pi/root/sys/env/tool/openjtalk/voice/htsvoice-tohoku-f01/tohoku-f01-happy.htsvoice'
#voice = '/home/pi/root/sys/env/tool/openjtalk/voice/akihiro0105/月音ラミ_1.0/月音ラミ_1.0.htsvoice'
#voice = '/home/pi/root/sys/env/tool/openjtalk/voice/MMDAgent_Example-1.8/Voice/takumi/takumi_normal.htsvoice'
voice = '/home/pi/root/sys/env/tool/openjtalk/voice/htsvoice-tohoku-f01/tohoku-f01-neutral.htsvoice'
if os.path.isfile(voice):
    engine = HTSEngine(voice.encode('utf-8'))
    labels = pyopenjtalk.extract_fullcontext(text)
    x = engine.synthesize(labels)
    sr = engine.get_sampling_frequency()
    ply = sa.play_buffer(x.astype(numpy.int16), 1, 2, sr)
    ply.wait_done()

