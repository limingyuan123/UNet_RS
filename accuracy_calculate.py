# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 20:35:07 2019

@author: HP
"""

import os
from tqdm import tqdm
from PIL import Image
import numpy as np

#获取目录下的文件名生成输入数据的路径
path = ("C:/Users/HP/Desktop/")
path1 = (path + "predicts/")    
os.chdir(path1)
predicts_path = os.listdir()
for i in range(0,len(predicts_path)):
    predicts_path[i] = path1 + predicts_path[i]     
path2 = (path + "validates/")    
os.chdir(path2)
validates_path = os.listdir()
for i in range(0,len(validates_path)):
    validates_path[i] = path2 + validates_path[i]  

# 每张图片生成子图的个数
for k in tqdm(range(len(predicts_path))):
    TP = 0
    FP = 0
    FN = 0
    TN = 0 
    predict = np.array(Image.open(predicts_path[k]).convert('L'))
    validate = np.array(Image.open(validates_path[k]).convert('L'))
    print(predicts_path[k])
    rows, cols = predict.shape
    for i in range(rows):
        for j in range(cols):
            if (predict[i,j] == 1 and validate[i,j] == 1):
                TP += 1
            elif (predict[i,j] == 1 and validate[i,j] == 0):
                FP += 1
            elif (predict[i,j] == 0 and validate[i,j] == 1):
                FN += 1
            elif (predict[i,j] == 0 and validate[i,j] == 0):
                TN += 1   
    accuracy = (TP+TN) / (TP+TN+FP+FN)
    precision = TP / (TP+FP)
    recall = TP / (TP+FN)
    quality = TP / (TP+FP+FN)    
    fmeasure = (2*precision*recall) / (precision+recall)       
    print("TP: %d" %TP)     
    print("FP: %d" %FP)
    print("FN: %d" %FN) 
    print("TN: %d" %TN)
    print("accuracy: %f" %accuracy)     
    print("precision: %f" %precision)
    print("recall: %f" %recall) 
    print("quality: %f" %quality)    
    print("fmeasure: %f" %fmeasure)     