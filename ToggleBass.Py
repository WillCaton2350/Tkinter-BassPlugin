from tkinter import *
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("700x500")
root.resizable(width=False,height=False)
root.title("AUD Toggle")
root['bg']='#000000'

style = ttk.Style()
style.theme_use("clam")

txt_Label = Label(root,bg="black",fg="yellow",text="Subwoofer")
txt_Label.place(x=50,y=30)

txt_Label.config(font=('Helvetica bold', 36))

txt_Label = Label(root, font=('Times', 45))

txt = tk.Text(root, height=1, width=25)
txt.pack(padx=2,pady=2)
txt.place(x=500,y=15)
txt.insert(tk.END, "")

search_Btn = Button(root,text="Go",fg="green",padx=1,pady=0.3)
search_Btn.pack()
search_Btn.place(x=465,y=15)

back_Ground_img = PhotoImage(file="/Users/mini/Desktop/Miscellaneous/r.png")
img = Label(root, image=back_Ground_img)
img.place(x=-1,y=70,relheight=1,relwidth=1)

imgs = PhotoImage(file="/Users/mini/Desktop/Miscellaneous/pics.png")

big_Btn = Button(root,bg="white",bd=0,image=imgs)
big_Btn.pack()
big_Btn.place(x=10,y=35)

bypass_Btn = Button(root,text="Bypass",padx=1,pady=1)
bypass_Btn.pack()
bypass_Btn.place(x=80,y=150)

feedback_Btn = Button(root,text="Feedback",padx=1,pady=1)
feedback_Btn.pack()
feedback_Btn.place(x=153,y=150)

# Vertical btns
L_Btn = Button(root,text="X-Verb",fg="red",padx=1,pady=1)
L_Btn.pack()
L_Btn.place(x=80,y=190)

Li_Btn = Button(root,text="i-Delay",fg="red",padx=1,pady=1)
Li_Btn.pack()
Li_Btn.place(x=80,y=230)

Lin_Btn = Button(root,text="X-Filter",fg="red",padx=1,pady=1)
Lin_Btn.pack()
Lin_Btn.place(x=80,y=270)

Line_Btn = Button(root,text="iX-Dirty",fg="red",padx=1,pady=1)
Line_Btn.pack()
Line_Btn.place(x=80,y=310)

Line_Btns = Button(root,text="Solo",fg="brown",padx=1,pady=1)
Line_Btns.pack()
Line_Btns.place(x=610,y=150)

Lines_Btns = Button(root,text="Mute",fg="red",padx=1,pady=1)
Lines_Btns.pack()
Lines_Btns.place(x=610,y=430)

def show():
    visual_Label = Label(root, text=clicked.get()).pack(padx=2,pady=0.5)

clicked = StringVar()
clicked.set("Toggle ⏻")

Presets = OptionMenu(root,clicked,"Trap Bass","Crown Wave Bass","Roland 808","Dark Sub Bass","Heavy E-Bass","Hard Knock 808","70's Bass","Pulse Synth Bass","Holy Sine Bass","Fyre 808")
Presets.pack(padx=1,pady=1)
Presets.place(x=240,y=151,relheight=0.041,relwidth=0.3)  

# SLIDERS

Mix = LabelFrame(root, bg="white",bd=0,fg="black", text="⏻ Master",padx=0,pady=0)
    
Mix.config(bg="black",fg="yellow")       
Mix.pack()

mix_Slider = ttk.Scale(Mix, from_=10,to=0, orient=VERTICAL)
mix_Slider.pack(padx=0,pady=50)
Mix.place(x=600,y=200)

root.mainloop()

