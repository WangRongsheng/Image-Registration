'''
读取dicom文件，并且在水平面、冠状面、矢状面任意面切割单个或者多个连续图像，并保存为jpg或png
'''

import pydicom
import cv2
import os

inputdir = './dicom/'
f = '094336_R_AP.dcm'
outdir = './test/'

dicom = pydicom.dcmread(inputdir + f)
img = dicom.pixel_array
# 坐标轴切割参考：https://codeantenna.com/a/pjoSVtbWZb
# 沿水平面切
img = img[749, :, :]
# 沿冠状面切
#img = img[:, 700, :]
# 沿矢状面切
#img = img[:, 100, :]
print("img", img.shape)
cv2.imwrite(outdir + f.replace('.dcm','.png'),img)

'''
img.shape
(750, 1023, 512)

img[0].shape
(1023, 512)

img[1, :, :]
(1023, 512)

img[:, 1, :]
(750, 512)

img[:, :, 1]
(750, 512)
'''
