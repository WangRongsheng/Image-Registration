## using simpleITK to load and save data.
import SimpleITK as sitk

filepath = './dcm/094336_R_AP.dcm'
itk_img = sitk.ReadImage(filepath)
img = sitk.GetArrayFromImage(itk_img)

## save 
out = sitk.GetImageFromArray(img)
#out.SetSpacing(itk_img.GetSpacing())
out.SetOrigin(itk_img.GetOrigin())
out.SetSpacing((0.13001,0.0924 , 0.2))
#out.SetSpacing((0.0924, 0.13001, 0.2))

print(itk_img.GetSpacing())
print(itk_img.GetOrigin())

sitk.WriteImage(out,'simpleitk_save3.dcm')