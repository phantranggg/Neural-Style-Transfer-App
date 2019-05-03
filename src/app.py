import tkinter as tk
from PIL import Image, ImageTk
from tkinter import filedialog as tkfd
import os

root = tk.Tk()
root.title("Neural style transfer")

canvas = tk.Canvas(root,width=1200,height=600)
canvas.pack()

dirname = os.path.dirname(__file__)
imgPath = os.path.join(dirname, './static/')

class Block:
	def __init__(self,root):
		img = Image.open(imgPath+'no-image.png')
		img = img.resize((300,300),Image.ANTIALIAS)
		self.img = ImageTk.PhotoImage(img)
		self.label = tk.Label(root,image=self.img)
		self.btn = tk.Button(root,text="Choose image",command=self.choose_img)
	
	def choose_img(self):
		f = tkfd.askopenfile(initialdir = imgPath,title = "Select image",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
		try:
			# TODO: check image in here
			img = Image.open(f)
			img = img.resize((300,300),Image.ANTIALIAS)
			self.img = ImageTk.PhotoImage(img)
			self.label.configure(image=self.img)
		except (Exception, e):
			print(str(e))
			pass

content = Block(canvas)
style = Block(canvas)

# specify image and button location
content.label.place(x=0,rely=0.1)
content.btn.place(x=100,y=450)

style.label.place(x=400,rely=0.1)
style.btn.place(x=500,y=450)

def transfer():
        #TODO: pass function in module model
	# use content.img & style.img as 2 inputs
	print("-----")

f = Image.open(imgPath+'arrow.png')
f = f.resize((100,100),Image.ANTIALIAS)
transferIcon = ImageTk.PhotoImage(f)
transferBtn = tk.Button(canvas,image=transferIcon,text="Transfer",command=transfer)
transferBtn.place(x=750,y=150)

f = Image.open(imgPath+'no-image.png')
f = f.resize((300,300),Image.ANTIALIAS)
generatedImg = ImageTk.PhotoImage(f)
transferLabel = tk.Label(canvas,image=generatedImg)
transferLabel.place(x=900,rely=0.1)

root.mainloop()
