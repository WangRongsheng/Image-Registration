import pydicom as dicom

DATA_PATH = './'

f = dicom.read_file(DATA_PATH + '094336_R_AP.dcm')
#print(f)

# 十六进制前缀：https://blog.csdn.net/mouday/article/details/107356090
#print(f[0X0010, 0X0010])
print('Pixel spacing(像素间距)：', f[0X0028, 0X0030].value)

#print(f[0X0010, 0X0020])
print('Spacing between slices(层间距)：', f[0X0018, 0X0088].value)