import time
import os
import shutil
import logging
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfile


root = Tk()
root.title = "WEFAX Decoder"
root.geometry("250x200")

support_formats = ["wav"]

logging.basicConfig(level=logging.DEBUG)

def load_file():
    try:
        dir_name = str(round(time.time() * 1000))
        save_directory = f"temp/{dir_name}"
        os.makedirs(save_directory)
        filename = askopenfile()
        while filename is not None and filename.name.split(".")[1] not in support_formats:
            filename = askopenfile()
            if filename is None:
                break
        if filename is not None:
            shutil.copy(filename.name, save_directory)
            return filename.name
        else:
            logging.info("Невозможно скопировать файл, т.к. файл не выбран")
        return None
    except Exception as e:
        print(e)
        return e


btn = ttk.Button(text="Load file", command=load_file)
btn.pack()

root.mainloop()