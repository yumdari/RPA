import os
from zlib import crc32
from tkinter import filedialog
from tkinter import messagebox

list_file = []                                          #파일 목록 담을 리스트 생성
files = filedialog.askopenfilename(initialdir="/",\
                 title = "파일을 선택 해 주세요") 

if files == '':
    messagebox.showwarning("경고", "파일을 추가 하세요")    #파일 선택 안했을 때 메세지 출력

f = open(files, 'rb')
data = f.read()
f.close()
 
crc = crc32(data)
print(hex(crc))
os.system("pause")