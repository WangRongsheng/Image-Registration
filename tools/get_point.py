from PIL import Image
import numpy as np
import cv2

img_L = np.array(Image.open('subtract.png').convert("L"))
#img_RGB = np.array(Image.open('subtract.png').convert("RGB"))

#这里得到灰度像素值0对应(0,0,0)
color_0_0_0 = np.where(img_L == 0)[0].shape[0]
pixel_sum = img_L.shape[0] * img_L.shape[1]
#print(img_L.shape[0])
#print(img_L.shape[1])

print("0_0_0 像素个数：{}\n总像素数：{} \n占比：{}%".format(color_0_0_0,pixel_sum*3,color_0_0_0/pixel_sum*3))
