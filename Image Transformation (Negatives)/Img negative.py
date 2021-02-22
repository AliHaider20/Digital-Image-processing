import matplotlib.pyplot as plt
import numpy as np
img = plt.imread('Wallpaper.jpg')

img = img.copy()

maxPixs = []
for row in img[:,:,0]:
   maxPixs.append(max(row))

maxPix = max(maxPixs)

choice = input('According to which channel Img negative is needed red, blue, green or all: ')
choice.lower()
def MakeNeg (img,maxpix,channel):
   if channel == 'red':
      ch = img[:,:,0]
      for row in range(len(ch[:])):
         for col in range(len(ch[0,:])):
            ch[row,col] = 255 - ch[row,col]

   if channel == 'blue':
      ch = img[:,:,1]
      for row in range(len(ch[:])):
         for col in range(len(ch[0,:])):
            ch[row,col] = 255 - ch[row,col]

   if channel == 'green':
      ch = img[:,:,2]
      for row in range(len(ch[:])):
         for col in range(len(ch[0,:])):
            ch[row,col] = 255 - ch[row,col]

   else:
      ch = img[:,:,0]
      for row in range(len(ch[:])):
         for col in range(len(ch[0,:])):
            ch[row,col] = 255 - ch[row,col]

      ch = img[:,:,1]
      for row in range(len(ch[:])):
         for col in range(len(ch[0,:])):
            ch[row,col] = 255 - ch[row,col]

      ch = img[:,:,2]
      for row in range(len(ch[:])):
         for col in range(len(ch[0,:])):
            ch[row,col] = 255 - ch[row,col]

   return ch

channel_neg = MakeNeg(img,255,choice)
plt.imsave('Img Negative acc to {0} channel.jpg'.format(choice),img)
