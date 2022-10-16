# coding=utf-8
# 导入python包
from skimage.metrics import structural_similarity as compare_ssim
from skimage.metrics import peak_signal_noise_ratio as compare_psnr
from skimage.metrics import normalized_mutual_information as compare_nmi
import matplotlib.pyplot as plt
import numpy as np
import cv2

def mse(imageA, imageB):
	# 计算两张图片的MSE指标
	err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
	err /= float(imageA.shape[0] * imageA.shape[1])
	
	# 返回结果，该值越小越好
	return err

def compare_images(imageA, imageB, title):
	# 分别计算输入图片的MSE和SSIM指标值的大小
	#m = mse(imageA, imageB)
	s = compare_ssim(imageA, imageB)

	# 创建figure
	fig = plt.figure(title)
	plt.suptitle("SSIM: %.2f" % (s))

	# 显示第一张图片
	ax = fig.add_subplot(1, 2, 1)
	plt.imshow(imageA, cmap = plt.cm.gray)
	plt.axis("off")

	# 显示第二张图片
	ax = fig.add_subplot(1, 2, 2)
	plt.imshow(imageB, cmap = plt.cm.gray)
	plt.axis("off")
	plt.tight_layout()
	plt.show()



# 读取图片
fixed = cv2.imread("200.png")
moving = cv2.imread("201.png")
affine = cv2.imread("affine_result.png")
subtract = cv2.imread("subtract.png")

# 将彩色图转换为灰度图
fixed = cv2.cvtColor(fixed, cv2.COLOR_BGR2GRAY)
moving = cv2.cvtColor(moving, cv2.COLOR_BGR2GRAY)
affine = cv2.cvtColor(affine, cv2.COLOR_BGR2GRAY)
subtract = cv2.cvtColor(subtract, cv2.COLOR_BGR2GRAY)

# 初始化figure对象
fig = plt.figure("Images")
images = ("fixed", fixed), ("moving", moving), ("affine", affine), ("subtract", subtract)

# 遍历每张图片
for (i, (name, image)) in enumerate(images):
	# 显示图片
	ax = fig.add_subplot(1, 4, i + 1)
	ax.set_title(name)
	plt.imshow(image, cmap = plt.cm.gray)
	plt.axis("off")
plt.tight_layout()
plt.show()

# 比较图片
compare_images(fixed, fixed, "fixed vs fixed")
compare_images(fixed, moving, "fixed vs moving")
compare_images(fixed, affine, "fixed vs affine")
compare_images(moving, affine, "moving vs affine")
compare_images(moving, subtract, "moving vs subtract")
compare_images(fixed, subtract, "fixed vs subtract")
compare_images(affine, subtract, "affine vs subtract")
