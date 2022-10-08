'''
import SimpleITK as sitk

filepath = './094336_R_AP.dcm'
file = sitk.ReadImage(filepath)
#reader = sitk.ImageSeriesReader()
#img_names = reader.GetGDCMSeriesFileNames(filepath)
#reader.SetFileNames(img_names)
#image = reader.Execute()
#image_array = sitk.GetArrayFromImage(image) # z, y, x

# 大小，坐标原点， 像素间距，方向
print(file.GetSize())
print(file.GetOrigin())
print(file.GetSpacing())
print(file.GetDirection())
spacing = file.GetSpacing()
origin = file.GetOrigin()
savedImg = sitk.GetImageFromArray(file)
savedImg.SetSpacing(spacing)
savedImg.SetOrigin(origin)
sitk.WriteImage(savedImg, '094336_R_AP.nii')
'''

## using simpleITK to load and save data.
import SimpleITK as sitk

filepath = './dcm/094336_R_AP.dcm'
itk_img = sitk.ReadImage(filepath)
img = sitk.GetArrayFromImage(itk_img)

## save 
out = sitk.GetImageFromArray(img)
#out.SetSpacing(itk_img.GetSpacing())
out.SetOrigin(itk_img.GetOrigin())
#out.SetSpacing((0.13001,0.0924 , 1.0))
out.SetSpacing((0.0924, 0.13001, 0.2))

print(itk_img.GetSpacing())
print(itk_img.GetOrigin())

sitk.WriteImage(out,'simpleitk_save2.nii.gz')