#!/usr/bin/env python3
# coding: utf8
import pyopenjtalk, numpy, os.path, glob
import simpleaudio as sa
class OpenJTalker:
    def __init__(self, htsvoice_dir_path=None):
        self.__engines = HtsEngineContainer(htsvoice_dir_path)
    @property
    def VoiceRootDir(self): return self.__engines.RootDir
    @property
    def VoiceNames(self): return self.__engines.Names
    def talk(self, text, param=None, save_path=None, **kwargs):
        ply = self.__talk(text, param=param, save_path=save_path)
        ply.wait_done()
    def talk_async(self, text, param=None, save_path=None):
        ply = self.__talk(text, param=param, save_path=save_path)
        return sa.play_buffer(x.astype(numpy.int16), 1, 2, sr)
        # if play_obj.is_playing(): play_ojb.stop()
    def __talk(self, text, param=None, save_path=None):
        engine, labels = self.__set_params(text, param)
        engine.synthesize_from_strings(labels)
        x = engine.get_generated_speech()
        if save_path: engine.save_riff(save_path.encode('utf-8'))
        engine.refresh()
        sr = engine.get_sampling_frequency()
        ply = sa.play_buffer(x.astype(numpy.int16), 1, 2, sr)
        return ply
    def __set_params(self, text, params):
        labels = pyopenjtalk.extract_fullcontext(text)
        if isinstance(labels, tuple) and len(labels) == 2: labels = labels[1]
        if params is None: return self.__engines.get(), labels
        engine = self.__engines.get(params.HtsVoice)
        engine.set_speed(params.Speed)
        engine.add_half_tone(params.HalfTone)
        if 1<=params.SamplingFrequency: engine.set_sampling_frequency(params.SamplingFrequency)
        if 1<=params.FramePeriod: engine.set_fperiod(params.FramePeriod)
        if 0.0 <= params.AllPass <= 1.0: engine.set_alpha(params.AllPass) 
        if 0.0 <= params.Postfiltering <= 1.0: engine.set_beta(params.Postfiltering) 
        if 0.0 <= params.Threshold <= 1.0: engine.set_msd_threshold(0, params.Threshold) # stream_index
        if 0.0 <= params.Weight: engine.set_gv_weight(0, params.Weight) # stream_index
        if 0.0 <= params.WeightF0: engine.set_gv_weight(1, params.WeightF0) # stream_index
        if 0.0 <= params.Volume: engine.set_volume(params.Volume)
        if 0.0 <= params.BufferSize: engine.set_audio_buff_size(params.BufferSize)
        return engine, labels
    def save(self, text, param=None, save_path='ojt.wav'):
        self.__save(text, param=param, save_path=save_path)
    def __save(self, text, param=None, save_path='ojt.wav'):
        engine, labels = self.__set_params(text, param)
        njd_results, labels = pyopenjtalk.run_frontend(text)
        engine.synthesize_from_strings(labels)
        engine.save_riff(save_path.encode('utf-8'))

class HtsEngineContainer: # HTSEngine(voice)で生成したインスタンスを保持しておく。
    def __init__(self, htsvoice_dir_path=None):
        self.__root_dir = htsvoice_dir_path
        self.__names = []
        self.__engines = {}
        self.__get_htsvoice_pathes()
    def __get_htsvoice_pathes(self):
        if self.__root_dir is not None and os.path.isdir(self.__root_dir):
            self.__pathes = glob.glob(os.path.join(self.__root_dir, '**/*.htsvoice'), recursive=True)
            for path in self.__pathes:
                self.__add_name_from_path(path)
    def __add_name(self, path, name):
        if name in self.__names: print(f'WARN: htsvoiceのファイル名が重複している。: {name}: {path}')
        else: self.__names.append(name)
        return name
    def __add_name_from_path(self, path):
        return self.__add_name(path, os.path.splitext(os.path.basename(path))[0])
    @property
    def RootDir(self): return self.__root_dir
    @property
    def Names(self): return self.__names
#    @property # 一気にすべてのエンジンを生成するとメモリ消費量が多いのでやらない
#    def Engines(self): return self.__engines
    # 遅延生成する。get()したときにはじめて生成する。既存ならそのまま返す。
    def get(self, name=None): # name: パスにある文字列のうち一意に特定できる文字列を渡す
        if name is None:
            if 'DEFAULT' not in self.__names: 
                self.__engines['DEFAULT'] = pyopenjtalk.HTSEngine(pyopenjtalk.DEFAULT_HTS_VOICE)
            return self.__engines['DEFAULT']
        elif name in self.__engines.keys(): return self.__engines[name]
        elif name in self.__names and name not in self.__engines.keys():
            for path in self.__pathes: # ファイル名
                if path.endswith(name + '.htsvoice'):
                    self.__engines[name] = pyopenjtalk.HTSEngine(path.encode('utf-8'))
                    return self.__engines[name]
            return None
        elif name in self.__pathes: # ファイルパス
            path = name
            name = self.__add_name_from_path(name)
            self.__engines[name] = pyopenjtalk.HTSEngine(path.encode('utf-8'))
            return self.__engines[name]
        else: # RootDirに存在しないが別のパスに存在する
            path = name
            if os.path.isfile(path):
                name = self.__add_name_from_path(name)
                self.__engines[name] = pyopenjtalk.HTSEngine(path.encode('utf-8'))
                return self.__engines[name]
            else: return None

class TalkParameter:
    def __init__(self, 
                   htsvoice=None,
                   speed=1.0, 
                   half_tone=0.0,
                   sampling_frequency=-1,
                   frame_period=-1,
                   all_pass=-1,
                   postfiltering=0.0,
                   threshold=0.5,
                   weight=1.0,
                   weight_f0=1.0,
                   volume=0.0,
                   buffer_size=0.0):
        self.__htsvoice = htsvoice
        self.__speed = speed 
        self.__half_tone = half_tone 
        self.__sampling_frequency = sampling_frequency 
        self.__frame_period = frame_period
        self.__all_pass = all_pass 
        self.__postfiltering = postfiltering 
        self.__threshold = threshold 
        self.__weight = weight 
        self.__weight_f0 = weight_f0 
        self.__volume = volume 
        self.__buffer_size = buffer_size 
        """
        """
        self.HtsVoice = htsvoice
        self.Speed = speed 
        self.HalfTone = half_tone 
        self.SamplingFrequency = sampling_frequency 
        self.FramePeriod = frame_period 
        self.AllPass = all_pass 
        self.Postfiltering = postfiltering 
        self.Threshold = threshold 
        self.Weight = weight 
        self.WeightF0 = weight_f0 
        self.Volume = volume 
        self.BufferSize = buffer_size 

    @property
    def HtsVoice(self): return self.__htsvoice
    @HtsVoice.setter
    def HtsVoice(self, v):
        if v is not None and os.path.isfile(v): self.__htsvoice = v
    @property
    def Speed(self): return self.__speed
    @Speed.setter
    def Speed(self, v):
        if 0 <= v: self.__speed = v
    @property
    def HalfTone(self): return self.__half_tone
    @HalfTone.setter
    def HalfTone(self, v): self.__half_tone = v
    @property
    def SamplingFrequency(self): return self.__sampling_frequency
    @SamplingFrequency.setter
    def SamplingFrequency(self, v):
        if 1 <= v: self.__sampling_frequency = v
#        else: self.__sampling_frequency = engine.get_sampling_frequency()
        else: self.__sampling_frequency = 48000
    @property
    def FramePeriod(self): return self.__frame_period
    @FramePeriod.setter
    def FramePeriod(self, v):
        if 1 <= v: self.__frame_period = v
#        else: self.__frame_period = 1
    @property
    def AllPass(self): return self.__all_pass
    @AllPass.setter
    def AllPass(self, v):
        if 0.0 <= v <= 1.0: self.__all_pass = v
    @property
    def Postfiltering(self): return self.__postfiltering
    @Postfiltering.setter
    def Postfiltering(self, v):
        if 0.0 <= v <= 1.0: self.__postfiltering = v
    @property
    def Threshold(self): return self.__threshold
    @Threshold.setter
    def Threshold(self, v):
        if 0.0 <= v <= 1.0: self.__threshold = v
    @property
    def Weight(self): return self.__weight
    @Weight.setter
    def Weight(self, v):
        if 0.0 <= v: self.__weight = v
    @property
    def WeightF0(self): return self.__weight_f0
    @WeightF0.setter
    def WeightF0(self, v):
        if 0.0 <= v: self.__weight_f0 = v
    @property
    def Volume(self): return self.__volume
    @Volume.setter
    def Volume(self, v): self.__volume = v
    @property
    def BufferSize(self): return self.__buffer_size
    @BufferSize.setter
    def BufferSize(self, v):
        if 0.0 <= v: self.__buffer_size = v

