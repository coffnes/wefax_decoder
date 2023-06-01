import time
import os
import shutil
import logging
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfile
from demodulator import Demodulator


root = Tk()
root.title = "WEFAX Decoder"
root.geometry("250x200")

support_formats = ["wav"]

logging.basicConfig(level=logging.DEBUG)

def load_file():
    try:
        file = askopenfile()
        filepath = file.name
        while file is not None and filepath.split(".")[1] not in support_formats:
            file = askopenfile()
            filepath = file.name

        if file is not None:
            dir_name = str(round(time.time() * 1000))
            save_directory = f"temp/{dir_name}"
            os.makedirs(save_directory)
            path = shutil.copy(filepath, save_directory)
            logging.info("Скопирован файл: " + filepath)
            d = Demodulator(path)
            print(d.__read_file())
            return filepath
        else:
            logging.info("Невозможно скопировать файл, т.к. файл не выбран")
        return None
    
    except Exception as e:
        print(e)
        return e


btn = ttk.Button(text="Загрузить файл", command=load_file)
btn.pack()

root.mainloop()