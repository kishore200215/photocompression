import PIL
from PIL import Image
from tkinter.filedialog import *
import os.path

def compress(filename):
    # file_path = askopenfilename()
    img = PIL.Image.open(filename)
    photoheight, photowidth = img.size

    img = img.resize((photoheight,photowidth),PIL.Image.ANTIALIAS)
    img.save('{}compressed.jpg'.format(filename))
