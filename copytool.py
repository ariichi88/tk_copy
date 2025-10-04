#! /usr/bin/env python3
# coding: UTF-8

import os
import shutil
import datetime
import tkinter as tk
import tkinter.filedialog as dialog
import tkinter.messagebox as message
from tkinter import ttk

FROM_DIR = '/home/*username*/Dropbox/カメラアップロード/'
TO_DIR_JPG = '/home/*username*/Dropbox/Photo/'
TO_DIR_MP4 = '/home/*username*/Dropbox/Videos/*yourmoviefolder*/'


def is_exist(old_name, kind):
    files = [f for f in os.listdir(FROM_DIR) if old_name in f]
    count = 0
    for _, file in enumerate(files):
        _, ext = os.path.splitext(file)
        if kind in ext:
            count = count + 1
    return count


def copy_files(old_name, to_dir, kind, new_name):
    from_files = [f for f in os.listdir(FROM_DIR) if old_name in f]
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
        self.pack(anchor=tk.W)
        # create & layout widget
        self.frame1 = ttk.Frame(self)
        self.frame1.pack(anchor=tk.W)
        self.from_label1 = ttk.Label(self.frame1, text='コピー元　　　　')
        self.from_label2 = ttk.Label(self.frame1, text=FROM_DIR)
        self.from_label1.pack(side=tk.LEFT)
        self.from_label2.pack(side=tk.LEFT)
        self.frame2 = ttk.Frame(self)
        self.frame2.pack(anchor=tk.W)
        self.date_label = ttk.Label(self.frame2, text='コピーする日付　')
        self.date_entry = ttk.Entry(self.frame2, width=10)
        self.date_change_btn = ttk.Button(self.frame2, text='反映')
        self.date_label.pack(side=tk.LEFT)
        self.date_entry.pack(side=tk.LEFT)
        self.date_change_btn.pack(side=tk.LEFT)
        self.frame3 = ttk.Frame(self)
        self.frame3.pack(anchor=tk.W)
        self.to_jpg_label = ttk.Label(self.frame3, text='コピー先（写真）')
        self.to_jpg_entry = ttk.Entry(self.frame3, width=40)
        self.to_jpg_btn = ttk.Button(self.frame3, text='参照')
        self.to_jpg_label.pack(side=tk.LEFT)
        self.to_jpg_entry.pack(side=tk.LEFT)
        self.to_jpg_btn.pack(side=tk.LEFT)
        self.frame4 = ttk.Frame(self)
        self.frame4.pack(anchor=tk.W)
        self.to_mp4_label = ttk.Label(self.frame4, text='コピー先（動画）')
        self.to_mp4_entry = ttk.Entry(self.frame4, width=40)
        self.to_mp4_btn = ttk.Button(self.frame4, text='参照')
        self.to_mp4_label.pack(side=tk.LEFT)
        self.to_mp4_entry.pack(side=tk.LEFT)
        self.to_mp4_btn.pack(side=tk.LEFT)
        self.frame5 = ttk.Frame(self)
        self.frame5.pack(anchor=tk.W)
        self.new_name_label = ttk.Label(self.frame5, text='新しい名前　　　')
        self.new_name_entry = ttk.Entry(self.frame5, width=30)
        self.new_name_label.pack(side=tk.LEFT)
        self.new_name_entry.pack(side=tk.LEFT)
        self.frame6 = ttk.Frame(self)
        self.frame6.pack(anchor=tk.E)
        self.rename_btn = ttk.Button(self.frame6, text='名前の変更・コピー')
        self.rename_btn.pack(side=tk.RIGHT)
        self.to_mp4_btn.pack(side=tk.LEFT)
        # init widget
        dt = datetime.datetime.now()
        date = dt.strftime('%Y/%m/%d')
        self.date_entry.insert(0, date)
        self.to_jpg_entry.insert(0, TO_DIR_JPG + date + '/')
        self.to_mp4_entry.insert(0, TO_DIR_MP4)
        self.date_change_btn['command'] = self.change_date_entry
        self.to_jpg_btn['command'] = self.open_jpg_dialog
        self.to_mp4_btn['command'] = self.open_mp4_dialog
        self.rename_btn['command'] = self.rename_copy_files

    def change_date_entry(self):
        var = TO_DIR_JPG + self.date_entry.get() + '/'
        self.to_jpg_entry.delete(0, tk.END)
        self.to_jpg_entry.insert(0, var)

    def open_jpg_dialog(self):
        choose = dialog.askdirectory(initialdir=TO_DIR_JPG)
        if choose:
            date = self.date_entry.get()
            self.to_jpg_entry.delete(0, tk.END)
            self.to_jpg_entry.insert(0, choose + '/'+ date)

    def open_mp4_dialog(self):
        choose = dialog.askdirectory(initialdir=TO_DIR_MP4)
        if choose:
            self.to_mp4_entry.delete(0, tk.END)
            self.to_mp4_entry.insert(0, choose)

    def rename_copy_files(self):
        old_name = self.date_entry.get().replace('/', '-')
        to_jpg = self.to_jpg_entry.get()
        to_mp4 = self.to_mp4_entry.get()
        new_name = self.new_name_entry.get()
        count_jpg = is_exist(old_name, 'jpg')
        count_mp4 = is_exist(old_name, 'mp4')
        if not new_name.strip():
            message.showwarning('警告', '新しい名前を入力してください')
            return
        if count_jpg:
            if os.path.exists(to_jpg):
                message.showerror('エラー', 'インポートできませんでした')
                count_jpg = 0
            else:
                os.makedirs(to_jpg)
                copy_files(old_name, to_jpg, 'jpg', new_name)
        if count_mp4:
            copy_files(old_name, to_mp4, 'mp4', new_name)
        if not count_jpg and not count_mp4:
            message.showinfo('コピー結果', 'コピーするファイルがありません')
            return
        result = '写真を{}個\n動画を{}個\nコピーしました'.format(count_jpg, count_mp4)
        message.showinfo('コピー結果', result)


if __name__ == '__main__':
    root = tk.Tk()
    root.title('Copy Tool')
    style = ttk.Style()
    style.theme_use('alt')
    app = Application(master=root)
    app.mainloop()
