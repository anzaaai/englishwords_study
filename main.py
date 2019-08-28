#!/usr/bin/env python
# -*- coding: utf8 -*-
import sys
import tkinter as tk
from mutagen.mp3 import MP3 as mp3
from pygame.locals import *
import pygame
import time
import random
import glob

# 画面作成
root = tk.Tk()
root.geometry('600x600')
root.title('えいたんごのべんきょう')

# 英単語定数
ENGLISH_WORDS_LIST = glob.glob('words/*')

# ボタンクリック
def play():
    filename = random.choice(ENGLISH_WORDS_LIST)
    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    mp3_length = mp3(filename).info.length 
    pygame.mixer.music.play(1)
    time.sleep(mp3_length + 0.25) 
    pygame.mixer.music.stop()    
    
# ボタン
btn = tk.Button(root, text='もんだい', command=play)
btn.pack(fill = 'x', padx=40,pady=200)



# テキストが表示されないバグのため画面を1px動かす
def fix():
    a = root.winfo_geometry().split('+')[0]
    b = a.split('x')
    w = int(b[0])
    h = int(b[1])
    root.geometry('%dx%d' % (w+1,h+1))
root.update()
root.after(0, fix)




root.mainloop()