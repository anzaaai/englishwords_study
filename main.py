#!/usr/bin/env python
# -*- coding: utf8 -*-
import sys
import tkinter as tk
from mutagen.mp3 import MP3 as mp3
from pygame.locals import *
import pygame
import time
import random


# 画面作成
root = tk.Tk()
root.geometry('600x600')
root.title('えいたんごのべんきょう')

# 英単語定数
ENGLISH_WORDS_LIST = ['dog','apple','elephant','cap','cat','paper','zebra','banana','money','butterfly','sleep','tree','number']

# ボタンクリック
def play():
	filename = './words/' + random.choice(ENGLISH_WORDS_LIST) + '.mp3' #再生したいmp3ファイル
	pygame.mixer.init()
	pygame.mixer.music.load(filename) #音源を読み込み
	mp3_length = mp3(filename).info.length #音源の長さ取得
	pygame.mixer.music.play(1) #再生開始。1の部分を変えるとn回再生(その場合は次の行の秒数も×nすること)
	time.sleep(mp3_length + 0.25) #再生開始後、音源の長さだけ待つ(0.25待つのは誤差解消)
	pygame.mixer.music.stop() #音源の長さ待ったら再生停止
        
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