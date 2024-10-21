#! /usr/bin/env python3
# coding: UTF-8

import os
import shutil
import tkinter as tk
import tkinter.filedialog as dialog
from tkinter import ttk

FROM_DIR = '/home/yuuichi/Dropbox/カメラアップロード/'
TO_DIR_JPG = '/home/yuuichi/Dropbox/Photo/'
TO_DIR_MP4 = '/home/yuuichi/Dropbox/Video/MyMovies/'


def copy_files(date, to_dir, kind, new_name):
    from_files = [f for f in os.listdir(FROM_DIR) if date in f]
    from_files.sort()
    count = 1
    for _, from_file in enumerate(from_files):
        _, ext = os.path.splitext(from_file)
        if kind in ext:
            to_file = new_name + '-' + format(count, '02') + ext
            shutil.copy2(FROM_DIR + from_file, to_dir + to_file)
            count = count + 1


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)


if __name__ == '__main__':
    root = tk.Tk()
    root.title('Copy Tool')
    root.geometry('550x200')
    style = ttk.Style()
    style.theme_use('alt')
    app = Application(master=root)
    app.mainloop()
