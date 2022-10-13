# input image 图片相减
import cv2
import numpy as np
#from google.colab.patches import cv2_imshow
#img = cv2.imread('..\\lena.jpg')[0:512,0:512] #截取部分，保证大小一致
#img2 = cv2.imread('..\\opencv-logo.png' )[0:512,0:512]

affine_image = cv2.imread('./affine_result.png')
fixed_image = cv2.imread('./200.png')
#moving_image= cv2.imread('./201.png')
affine_image = affine_image.astype(np.float32) # uint8
fixed_image = fixed_image.astype(np.float32)

print('===================================')
print(type(affine_image))
print(affine_image.dtype)
print(affine_image.shape)
print(fixed_image.shape)
print('===================================')

affine_image = affine_image*1.9
affine_image = affine_image.astype(np.uint8) # float32
fixed_image = fixed_image.astype(np.uint8)

# 将矩阵保存成文本，数字格式为整数
#np.savetxt('lena_gray.txt', np.array(affine_image), fmt='%4d')

subtract_img = cv2.subtract(affine_image,fixed_image)
cv2.imwrite('subtract.png', subtract_img)