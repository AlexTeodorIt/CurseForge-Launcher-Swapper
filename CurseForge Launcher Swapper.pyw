#importing library
from tkinter import *
from tkinter import font
from PIL import ImageTk, Image 
import time
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter import messagebox
import shutil
from tkinter.messagebox import showinfo
import os
from pathlib import Path
import urllib.request
import ssl
import wget

user = (os.getlogin())


ssl._create_default_https_context = ssl._create_unverified_context
url1 = 'https://www.dropbox.com/s/yobqdh63eq38ya4/c1.png?dl=1'
url2 = 'https://www.dropbox.com/s/nkjbiap7ecjhu02/c2.png?dl=1'

PATH2 = r"C:/Users/" + user + r"/AppData/Local/Temp/c2.png"
PATH1 = r"C:/Users/" + user + r"/AppData/Local/Temp/c1.png"

if os.path.isfile(PATH1) and os.access(PATH1, os.R_OK):
    print("File exists and is readable ")
else:
    print("Either the file is missing or not readable ")
    #urllib.request.urlretrieve("https://www.dropbox.com/s/yobqdh63eq38ya4/c1.png?dl=1", "C:/Users/" + user + "/AppData/Local/Temp/c2.png")
    wget.download(url1, PATH1)


if os.path.isfile(PATH2) and os.access(PATH2, os.R_OK):
    print("File exists and is readable ")
else:
    print("Either the file is missing or not readable ")
    #urllib.request.urlretrieve("https://www.dropbox.com/s/nkjbiap7ecjhu02/c2.png?dl=1", "C:/Users/" + user + "/AppData/Local/Temp/c1.png")
    wget.download(url2, PATH2)

w=Tk()

#Using piece of code from old splash screen
width_of_window = 427
height_of_window = 250
screen_width = w.winfo_screenwidth()
screen_height = w.winfo_screenheight()
x_coordinate = (screen_width/2)-(width_of_window/2)
y_coordinate = (screen_height/2)-(height_of_window/2)
w.geometry("%dx%d+%d+%d" %(width_of_window,height_of_window,x_coordinate,y_coordinate))
#w.configure(bg='#ED1B76')
w.overrideredirect(1) #for hiding titlebar

#new window to open
def new_win():
    root = Tk()
    root.title('CF Launcher Replacer')
    #root.resizable(False, False)
    root.geometry('300x150')
    root.configure(bg='#272727')
    root.eval('tk::PlaceWindow . center')
    root.overrideredirect(1)


    

    open_button = Button(
        root,
        text='Replace File',
        command=select_file,
        bg='#949494'
    )


    B1 = Button(root, text = "Download SKLauncher", command = hello, bg='#949494')
    B1.place(x = 89,y = 30)

    B2 = Button(root, text = "Download CurseForge Launcher", command = curseforge_dl, bg='#949494')
    B2.place(x = 61,y = 95)

    B3 = Button(root, text = "Help", command = help, bg='#949494')
    B3.place(x = 2,y = 125)

    open_button.pack(expand=True)

def help():
    os.system("start \"\" https://github.com/al3xutzu34/CurseForge-Launcher-Swapper")

def curseforge_dl():
    urllib.request.urlretrieve("https://www.dropbox.com/s/d3ujapx4b2zbgvz/CurseForge.exe?dl=1", "C:/Users/" + user +"/AppData/Local/Temp/curseforge.exe")
    messagebox.showinfo("CurseForge Downloaded", "CurseForge has been successfully downloaded, it will be executed !")
    os.startfile("C:/Users/" + user +"/AppData/Local/Temp/curseforge.exe")

def hello():
    urllib.request.urlretrieve("https://www.dropbox.com/scl/fi/ffc5erjxt2uwfbbqgzy7n/minecraft.exe?rlkey=ldxwhj43jlk5h20vtjun91nvh&st=x9suvbd5&dl=1", "C:/Users/" + user +"/AppData/Local/Temp/minecraft.exe")
    messagebox.showinfo("SKLauncher Downloaded", "SKLauncher has been successfully downloaded !")

def select_file():
    # filetypes = (
        # ('Minecraft Launcher', 'minecraft.exe'),
    # )

    # filename = fd.askopenfilename(
        # title='Open a file',
        # initialdir='/',
        # filetypes=filetypes)

    # showinfo(
        # title='Selected File',
        # message=filename
    # )

    filename = ("C:/Users/" + user +"/AppData/Local/Temp/minecraft.exe")

    source = (filename)
    
    # Destination path
    destination = ("C:/Users/" + user + "/curseforge/minecraft/Install/minecraft.exe")

    shutil.move(source, destination)
    messagebox.showinfo("Launcher Swapped", "The Default Launcher has been swapped to SKLauncher !")

Frame(w, width=427, height=250, bg='#272727').place(x=0,y=0)
label1=Label(w, text='CurseForge Launcher Swapper', fg='white', bg='#272727') #decorate it 
label1.configure(font=("Game Of Squids", 19, "bold"))   #You need to install this font in your PC or try another one
label1.place(x=20,y=90)

label2=Label(w, text='Loading...', fg='white', bg='#272727') #decorate it 
label2.configure(font=("Calibri", 11))
label2.place(x=10,y=215)

#making animation

image_a=ImageTk.PhotoImage(Image.open(r"C:/Users/" + user + r"/AppData/Local/Temp/c2.png"))
image_b=ImageTk.PhotoImage(Image.open(r"C:/Users/" + user + r"/AppData/Local/Temp/c1.png"))




for i in range(5): #5loops
    l1=Label(w, image=image_a, border=0, relief=SUNKEN).place(x=180, y=145)
    l2=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=200, y=145)
    l3=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=220, y=145)
    l4=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=240, y=145)
    w.update_idletasks()
    time.sleep(0.5)

    l1=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=180, y=145)
    l2=Label(w, image=image_a, border=0, relief=SUNKEN).place(x=200, y=145)
    l3=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=220, y=145)
    l4=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=240, y=145)
    w.update_idletasks()
    time.sleep(0.5)

    l1=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=180, y=145)
    l2=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=200, y=145)
    l3=Label(w, image=image_a, border=0, relief=SUNKEN).place(x=220, y=145)
    l4=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=240, y=145)
    w.update_idletasks()
    time.sleep(0.5)

    l1=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=180, y=145)
    l2=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=200, y=145)
    l3=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=220, y=145)
    l4=Label(w, image=image_a, border=0, relief=SUNKEN).place(x=240, y=145)
    w.update_idletasks()
    time.sleep(0.5)



w.destroy()
new_win()
w.mainloop()
