from PIL import Image
import os
import glob

imagename = input('Image name here = ')
name_of_the_app = input(
    "What's the name of your app? => ") + '/assets/launcher/'
os.makedirs(name_of_the_app)

im = Image.open(imagename)
im = im.resize((1024, 1024))
im.save(name_of_the_app + 'icon.png')
im.save(name_of_the_app + 'foreground.png')
im.save(name_of_the_app + 'background.png')
