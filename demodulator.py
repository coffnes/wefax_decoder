from scipy.io import wavfile
import os
import logging
import numpy as np

logging.basicConfig(level=logging.DEBUG)

class Demodulator:
    def __init__(self, filepath: str, lines_per_minute: int = 120):

        if not os.path.exists(filepath):
            raise Exception(f"НЕПРАВИЛЬНЫЙ ФАЙЛ: файла по пути {filepath} не существует")


        self.filepath = filepath
        self.filename = self.filepath.split('/')[-1]
        self.lines_per_minute = lines_per_minute
        self.time_for_one_frame = 1 / (self.lines_per_minute / 60) 

    def file_info(self):
        sample_rate, data = wavfile.read(self.filepath)
        channels = len(data.shape)
        length = len(data) / sample_rate
        return{"filename": self.filename, "channels": channels, "sample_rate": sample_rate, "length": length}
    
    def process(self):
        self.audio_data, self.sample_rate, self.length = self.__read_file()
        print(self.audio_data, self.sample_rate, self.length)

    def __read_file(self):
        sample_rate, data = wavfile.read(self.filepath)

        if len(data.shape) == 2:
            logging.warning("Обнаружен двух канальный аудиофаил. Программа попытается соединить аудио в один канал")
            logging.info("СОЕДИНЕНИЕ АУДИО КАНАЛОВ")
            data = self.__merge_channels(data)

        length = len(data) / sample_rate
        return data, sample_rate, length
    
    def __merge_channels(self, audio_channels):
        parts = len(audio_channels)
        one_channel_audio = []
        for p in range(parts):
            one_channel_audio.append(np.divide(np.add(audio_channels[p][0], audio_channels[p][1]), 2))
        return one_channel_audio