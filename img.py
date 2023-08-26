from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
import os

window = Tk()
window.geometry("600x600")
window.configure(background = "black")

label_img = Label(window, bg = "white", highlightthickness = 5)
label_img.place(relx = 0.5, rely = 0.5, anchor = CENTER)

img_path = ""

def openImg():
    global img_path
    img_path = filedialog.askopenfilename(title = "Open Image File", filetypes = [("Image Files", "*.jpg *.png *.gif *.jpeg *.jfif *.jpe")])
    print(img_path)
    im = Image.open(img_path)
    img = ImageTk.PhotoImage(im)
    name = os.path.basename(img_path)
    formated_name = name.split('.')[0]
    window.title(formated_name)
    label_img["image"] = img
    img.close()
    
open_btn = Button(window, text = "Open Image", bg = "Grey", fg = "white", font = ("castellar", 15, "bold"), padx = 15, pady = 10, relief = SOLID, command = openImg)
open_btn.place(relx = 0.5, rely = 0.1, anchor = CENTER)

window.mainloop()