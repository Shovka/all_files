from tkinter import *
import pyscreenrec

root = Tk()
root.geometry("400x600")
root.title("Screen recorder")
root.config(bg="#fff")
root.resizable(False,False)


rec = pyscreenrec.ScreenRecorder()

#icon
image_icon = PhotoImage(file="./imgs/icon.jpg")
root.iconphoto(False,image_icon)

#background images
image1 = PhotoImage(file="./imgs/yellow.jpg")
Label(root,image=image1, bg="#fff").place(x=2,y=35)

# background images2
image1 = PhotoImage(file="./imgs/icon.jpg.jpg")
Label(root,image=image1, bg="#fff").place(x=2,y=35)

root.mainloop()