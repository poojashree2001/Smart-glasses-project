import tkinter
from tkinter.ttk import *
from tkinter import filedialog as fd 
from PIL import ImageTk, Image
import pytesseract
import re
from gtts import gTTS
import os
from googletrans import Translator
import  vlc
import time
def ocr_code(file_path):
    from PIL import Image
    import pytesseract
    import re
    from gtts import gTTS
    import os
    from googletrans import Translator
    import  vlc
    import time
    img = Image.open(file_path)
    text = pytesseract.image_to_string(img)
    #print(text.strip())
    text1=''
    translator=Translator()
    for k in text.split("\n"):
        if k=='\n':
            text1+=' '
            continue
        s=re.sub(r"[^a-zA-Z0-9]+", ' ', k)
        text1=text1+s
    print(text1)
    language = 'en'
    txt = gTTS(text=text1, lang=language, slow=False)
    txt.save("speech_english_t.mp3")
    p=vlc.MediaPlayer('speech_english_t.mp3')
    p.play()
    print('Done')
    
    
