import speech_recognition
import pyttsx3
import pyperclip
import pyautogui
from PIL import ImageTk
import PIL.Image
import os
import uuid
from tkinter import *
import tkinter as tk
import tkinter.font as font
#import ctypes
#ctypes.windll.user32.ShowWindow( ctypes.windll.kernel32.GetConsoleWindow(), 0 )

def my_function():
    u = uuid.UUID(int=uuid.getnode())
    print(u)
    print("Start:")
    recognizer = speech_recognition.Recognizer()
    text =""
    if len(text)==0:
        try:
            with speech_recognition.Microphone() as mic:
                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)

                text = recognizer.recognize_google(audio,language="ar-AR")
                print("Recognized {}".format(text))
                pyperclip.copy(" "+text+" ")
                # Hotkey the paste command
                pyautogui.hotkey("ctrl", "v")
                text =""
        except speech_recognition.UnknownValueError():
            recognizer = speech_recognition.Recognizer()
            text = ""

# create a tkinter window
root = Tk()
root.title('محوّل الصوت إلى كتابة')
root.iconbitmap('icon.ico')
root.geometry('300x400')
#if "00000000-0000-0000-0000-201a06de76be" == str(uuid.UUID(int=uuid.getnode())):
if 1 == 1:
    print("yess")
    myFont = font.Font(size=30)
    title_font = font.Font(size=20, weight="bold")

    text = Label( text="محوّل الصوت إلى كتابة" )
    text.place(relx=0.5, rely=0.1, anchor=CENTER)
    text['font'] = title_font

    btn_text = tk.StringVar()
    btn = Button(root, text='بداية التسجيل' , bd='5',bg='green',activebackground='red',fg='white',command=my_function)
    btn['font'] = myFont

    btn.place(relx=0.5, rely=0.8, anchor=CENTER)

    image = PIL.Image.open('background.jpg')
    zoom = 0.35

    pixels_x, pixels_y = tuple([int(zoom * x)  for x in image.size])
    img = ImageTk.PhotoImage(image.resize((pixels_x, pixels_y)))
    label = Label(root, image=img)
    label.image = img
    label.place(relx=0.5, rely=0.4, anchor=CENTER)
else:
    print('')
    myFont = font.Font(size=30)
    title_font = font.Font(size=20, weight="bold")

    text = Label(text="برنامجك غير مفعل !")
    text.place(relx=0.5, rely=0.3, anchor=CENTER)
    text['font'] = title_font

    text = Label(text="إتصل بنا للحصول على التفعيل")
    text.place(relx=0.5, rely=0.5, anchor=CENTER)
    text['font'] = title_font

    text = Label(text="0556069522")
    text.place(relx=0.5, rely=0.7, anchor=CENTER)
    text['font'] = title_font


root.mainloop()

