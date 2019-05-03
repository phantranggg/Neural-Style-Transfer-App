from tkinter import *
from tkinter import filedialog as tkfd
from PIL import Image, ImageTk
import os

contentImage = None
styleImage = None

top = Tk()
top.geometry("1200x600")
top.resizable(0,0)

dirname = os.path.dirname(__file__)

popularStylePath = os.path.join(dirname, './static/popular_style/')

def createImage(imgPath,size):
    try:
        img = Image.open(imgPath)
        img = img.resize(size,Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        return img
    except Exception as ex:
        print(ex)

class PopularStyle:
    def __init__(self,imgName,pWidget,x,y):
        self.img = createImage(popularStylePath+imgName,size=(125,125))
        self.btn = Button(pWidget,image=self.img,command=self.setStyle)
        self.btn.place(x=x,y=y)
    
    def setStyle(self):
        global styleImage
        styleImage = self.img


imgPath = os.path.join(dirname, './static/')

class Upload:
    def __init__(self,imgName,pWidget,imgType):
        self.imgType = imgType
        self.img = createImage(imgPath+imgName,size=(300,300))
        self.btn = Button(pWidget,image=self.img,command=self.uploadImage)
        self.btn.pack()
    
    def uploadImage(self):
        global styleImage,contentImage
        f = tkfd.askopenfile(initialdir = imgPath,title = "Select image",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
        try:
            self.img = createImage(f.name,size=(300,300))
            self.btn.configure(image=self.img)
            if self.imgType == 'content':
                contentImage = self.img
            elif self.imgType == 'style':
                styleImage = self.img
        except Exception as ex:
            print(ex)
            pass

# content
cUploadContent = Canvas(top,height=300,width=300)
cUploadContent.place(x=50,y=100)

uploadStyle = Upload('no-image.png',cUploadContent,imgType='content')
contentLabel = Label(top,text="Content Image")
contentLabel.place(x=170,y=420)
# =============

# style
styleFlag = True    # open popular style
def togglePopularStyle():
    global styleFlag
    styleFlag = True
    if styleFlag:
        Misc.lift(cPopularStyle)

def toggleUploadStyle():
    global styleFlag
    styleFlag = False
    if not styleFlag:
        Misc.lift(cUploadStyle)

popularStyleBtn = Button(top,text="Popular Style",command=togglePopularStyle)
popularStyleBtn.place(x=400,y=50)

uploadStyleBtn = Button(top,text="Upload style",command=toggleUploadStyle)
uploadStyleBtn.place(x=550,y=50)

cUploadStyle = Canvas(top,height=300,width=300)
cUploadStyle.place(x=400,y=100)

cPopularStyle = Canvas(top,height=300,width=300)
cPopularStyle.place(x=400,y=100)

styleLabel = Label(top,text="Style Image")
styleLabel.place(x=520,y=420)

uploadStyle = Upload('no-image.png',cUploadStyle,imgType='style')

style_1 = PopularStyle('1.jpg',cPopularStyle,x=10,y=10)
style_2 = PopularStyle('2.jpg',cPopularStyle,x=165,y=10)
style_3 = PopularStyle('3.jpg',cPopularStyle,x=10,y=165)
style_4 = PopularStyle('4.jpg',cPopularStyle,x=165,y=165)

# ==============

def transfer():
    #TODO: pass function in module model
	# use contentImage & styleImage as 2 inputs
	print("-----")

transferIcon = createImage(imgPath+'arrow.png',size=(100,100))
transferBtn = Button(top,image=transferIcon,text="Transfer",command=transfer)
transferBtn.place(x=735,y=200)

generatedImg = createImage(imgPath+'no-image.png',size=(300,300))
transferLabel = Label(top,image=generatedImg)
transferLabel.place(x=875,y=100)
generatedLabel = Label(top,text="Transfer Image")
generatedLabel.place(x=1000,y=420)

top.mainloop()