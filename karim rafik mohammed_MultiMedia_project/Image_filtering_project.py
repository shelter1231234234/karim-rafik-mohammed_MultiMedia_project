from tkinter import *
from tkinter import filedialog   
from PIL import Image, ImageTk, ImageOps, ImageFilter

def open_image():
    global img, img_display
    file_path = filedialog.askopenfilename()
    if not file_path:
        return
    img = Image.open(file_path)
    show_image(img)

def save_image():
    if img:
        save_path = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg;*.jpeg"), ("All files", "*.*")]
        )
        if save_path:
            img.save(save_path)
            print(f"Image saved as {save_path}")

def to_grayscale():
    global img
    if img:
        img = ImageOps.grayscale(img)
        show_image(img)

def blur_image():
    global img
    if img:
        img = img.filter(ImageFilter.BLUR)
        show_image(img)

def invert_image():
    global img
    if img:
        img = ImageOps.invert(img.convert("RGB"))
        show_image(img)

def classic_brownish_image():
    global img
    if img:
        classic_brownish = ImageOps.colorize(ImageOps.grayscale(img), "#704214", "#C0A080")
        img = classic_brownish
        show_image(img)

def rotate_image():
    global img
    if img:
        img = img.rotate(90, expand=True)
        show_image(img)

def show_image(img):
    global img_display
    max_width = 800
    max_height = 600
    scale = min(max_width / img.width, max_height / img.height, 1)
    display_width = int(img.width * scale)
    display_height = int(img.height * scale)
    img_display = img.resize((display_width, display_height), Image.Resampling.LANCZOS)
    canvas.config(width=display_width, height=display_height)
    img_tk = ImageTk.PhotoImage(img_display)
    canvas.create_image(0, 0, anchor="nw", image=img_tk)
    canvas.image = img_tk

root = Tk()
root.title("Image Filter App")
canvas = Canvas(root)
canvas.pack()
Button(root, text="Open Image", command=open_image).pack()
Button(root, text="Grayscale", command=to_grayscale).pack()
Button(root, text="Blur", command=blur_image).pack()
Button(root, text="Invert Colors", command=invert_image).pack()
Button(root, text="classic_brownish", command=classic_brownish_image).pack()
Button(root, text="Rotate 90°", command=rotate_image).pack()
Button(root, text="Save Image", command=save_image).pack()
img = None
img_display = None
root.mainloop()
