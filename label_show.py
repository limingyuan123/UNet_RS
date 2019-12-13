# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 22:26:08 2019

@author: zzx
"""

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
img=np.array(Image.open('E:/deeplearning/深度学习-图像语义分割-工作进展/UNet/predict/pre1.png').convert('L'))

rows,cols=img.shape
for i in range(rows):
    for j in range(cols):
        if (img[i,j]!=0):
            img[i,j]=255
            
new_im = Image.fromarray(img.astype(np.uint8))
new_im.save('E:/deeplearning/深度学习-图像语义分割-工作进展/UNet/new2.png')
            
plt.imshow(img,cmap='gray')
plt.axis('off')
plt.show()