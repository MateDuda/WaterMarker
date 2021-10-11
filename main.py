from tkinter import *
from tkinter import filedialog

from PIL import ImageTk, Image

root = Tk()
root.resizable(width=True, height=True)
global img1, img2, dx, dy


def change_img(image):
    img = ImageTk.PhotoImage(image)
    panel.configure(image=img)
    panel.image = img
    panel.grid(row=2, column=0, columnspan=4)


def open_img():
    global img1
    x = filedialog.askopenfilename(title='open')
    img1 = Image.open(x)
    img1 = img1.resize((600, 600), Image.ANTIALIAS)
    change_img(img1)


def add_img():
    global img1, img2, dx, dy
    dx = 0
    dy = 0
    y = filedialog.askopenfilename(title='open')
    img2 = Image.open(y)
    img2 = img2.resize((200, 200), Image.ANTIALIAS)
    img1_c = img1.copy()
    img1_c.paste(img2, (dx, dy))
    change_img(img1_c)


def bigger():
    global img2, img1
    sizes = img2.size
    img2 = img2.resize((sizes[0] + 20, sizes[1] + 20), Image.ANTIALIAS)
    img1_c = img1.copy()
    img1_c.paste(img2, (dx, dy))
    change_img(img1_c)


def smaller():
    global img2, img1
    sizes = img2.size
    img2 = img2.resize((sizes[0] - 20, sizes[1] - 20), Image.ANTIALIAS)
    img1_c = img1.copy()
    img1_c.paste(img2, (dx, dy))
    change_img(img1_c)


def right():
    global img1, img2, dx, dy
    img1_c = img1.copy()
    dx += 20
    img1_c.paste(img2, (dx, dy))
    change_img(img1_c)


def left():
    global img1, img2, dx, dy
    img1_c = img1.copy()
    dx -= 20
    img1_c.paste(img2, (dx, dy))
    change_img(img1_c)


def down():
    global img1, img2, dx, dy
    img1_c = img1.copy()
    dy += 20
    img1_c.paste(img2, (dx, dy))
    change_img(img1_c)


def up():
    global img1, img2, dx, dy
    img1_c = img1.copy()
    dy -= 20
    img1_c.paste(img2, (dx, dy))
    change_img(img1_c)


def save():
    global img1, img2, dx, dy
    img1_c = img1.copy()
    img1_c.paste(img2, (dx, dy))
    img1_c.save('Watermarked.jpg')


panel = Label(root)
btn1 = Button(root, text='open image', command=open_img).grid(row=0, column=0)
btn2 = Button(root, text='add watermark', command=add_img).grid(row=1, column=0)
btn_size_down = Button(root, text='Bigger', command=bigger).grid(row=0, column=1)
btn_size_up = Button(root, text='Smaller', command=smaller).grid(row=1, column=1)
btn_left = Button(root, text="Left", command=left).grid(row=0, column=2)
btn_right = Button(root, text="Right", command=right).grid(row=1, column=2)
btn_up = Button(root, text="Up", command=up).grid(row=0, column=3)
btn_down = Button(root, text="Down", command=down).grid(row=1, column=3)
btn_save = Button(root, text="Save", command=save).grid(row=3, column=1, columnspan=2)

root.mainloop()
