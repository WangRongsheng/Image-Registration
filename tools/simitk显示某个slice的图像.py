import SimpleITK as sitk
import matplotlib.pyplot as plt

DATA_PATH = './'

#获取Dicom数据
ds = sitk.ReadImage(DATA_PATH + '094336_R_AP.dcm')
img_array = sitk.GetArrayFromImage(ds)
print(img_array.shape)
plt.imshow(img_array[0],cmap="gray")
plt.show()
