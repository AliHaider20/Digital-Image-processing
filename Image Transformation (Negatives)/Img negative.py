import matplotlib.pyplot as plt

img = plt.imread('Original.jpg')

img = img.copy()

maxPixs = []
for row in img[:,:,0]:
   maxPixs.append(max(row))

maxPix = max(maxPixs)

for gray_intensity in range(10):
   if (2**gray_intensity-1) == maxPix:
      break
      
L = 2**gray_intensity - 1
print("Image Intensity :",L)

choice = input('According to which channel Img negative is needed red, blue, green or all: ')
choice = choice.lower()

def MakeNeg (img,L,channel):
   if channel == 'red':
      ch = img[:,:,0]
      for row in range(len(ch[:])):
         for col in range(len(ch[0,:])):
            ch[row,col] = 255 - ch[row,col]

   if channel == 'green':
      ch = img[:,:,1]
      for row in range(len(ch[:])):
         for col in range(len(ch[0,:])):
            ch[row,col] = 255 - ch[row,col]

   if channel == 'blue':
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

channel_neg = MakeNeg(img,L,choice)
plt.imsave(f'Img Negative acc to {choice} channel.jpg',img)
