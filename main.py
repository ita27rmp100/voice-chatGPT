from tkinter import *
from voiceChatGPT import *
t = Tk()
t.title("VoiceGPT")
t.overrideredirect(TRUE)
# postion and geometry
screen_width = t.winfo_screenwidth()
screen_height = t.winfo_screenheight()
t.geometry(f"150x50+{screen_width-150}+{screen_height-93}")
# over all
t.attributes("-topmost",True)
# Button to ask
start = Button(t,text="ASK",command=discuss,bg="orange",width='20',height='3').place(x=0,y=0)
t.mainloop()