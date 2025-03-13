import tkinter
from tkinter.ttk import *
from tkinter import filedialog as fd 
from PIL import ImageTk, Image
import os
import imageToText
from gtts import gTTS
import os
from googletrans import Translator
import  vlc
import time
import main_video
import obj_detection
def ocr_load():
    import cv2
    cam = cv2.VideoCapture(0)
    cv2.namedWindow("test")
    img_counter = 0
    while True:
        ret, frame = cam.read()
        if not ret:
            print("failed to grab frame")
            break
        cv2.imshow("test", frame)
        k = cv2.waitKey(1)
        if k%256 == 27:
            # ESC pressed
            print("Escape hit, closing...")
            break
        elif k%256 == 32:
            # SPACE pressed
            img_name = "Clicked_image.jpg"
            cv2.imwrite(img_name, frame)
            print("{} written!".format(img_name))
            cam.release()
            cv2.destroyAllWindows()
            imageToText.ocr_code(img_name)

 
master=tkinter.Tk()
master.title("All in one")
master.geometry("450x350")

button1=tkinter.Button(master, text="Image to text", command=ocr_load)
button2=tkinter.Button(master, text="Object Detection", command=obj_detection.object_detect)
button3=tkinter.Button(master, text="Face Rec", command=main_video.main_face)
button1.grid(row=0,column=0)
button2.grid(row=1,column=0)
button3.grid(row=2,column=0)


master.mainloop()
