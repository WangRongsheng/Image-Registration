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

If you have a MacOS computer with Homebrew or MacPorts you can run brew install dcm2niix or sudo port install dcm2niix, respectively.
If you have Conda, conda install -c conda-forge dcm2niix on Linux, MacOS or Windows.
If you have pip, python -m pip install dcm2niix on Linux, MacOS or Windows.
On Debian Linux computers you can run sudo apt-get install dcm2niix.


1、-f 输出文件名：（例如“-f myMR”, 默认 '%f_%p_%t_%s'）dcm2niix允许您指定转换后的 NIfTI 文件的命名方式。该方法可能一开始看起来很复杂，但它提供了非常大的灵活性。
一个简单的文件名可能是“exp03subj09”。
在这种情况下，这个参与者的第一个序列将被命名为exp03subj09.nii，
接下来是exp03subj09a.nii，然后是exp03subj09b.nii等等。
但是

dcm2niix还允许您将相关信息的存在和位置标注到文件名中。
考虑您指定“exp03subj09%p%s” 
在这种情况下，协议的名称和序列号（存储在DICOM文件中）将成为文件名的一部分。
在这种情况下，输出文件的名称可能是exp03subj09fmri1.nii、
exp03subj09t12.nii
和exp03subj09fmri3.nii。
您可以按任意顺序组合尽可能多的修饰符。
以下是特殊修饰符的列表：

%a：插入天线（线圈）编号。例如，“myName％a”的输出文件名将生成“myName1”，“myName2”等，每个线圈一个。请注意，大多数扫描都会将所有线圈的数据组合在一起，在这些情况下，该选项将被忽略。例如，大多数将所有线圈的数据组合在一起的扫描通常只称为“myName”。
%d：插入系列描述（0008,103E）。例如，使用“myName％d”转换的回波平面图像会产生“myNameEPI”
%e：插入回波数。例如，具有两个回波时间的序列使用输出文件名“myName％e”进行转换，将产生“myName1”和“myName2”。请注意，大多数MRI序列仅使用单个回波时间，在这种情况下，您只会得到“myName1”。
%f：插入输入文件夹名。例如，使用输入文件夹“/usr/Subj22”和输出文件名“myName％f”将导致输出文件命名为“myNameSubj22.nii”。
%i：插入病人ID（DICOM标签0010,0020）。例如，“myName％i”的输出文件名将把病人ID命名为“ID123”的图像转换为“myNameID123.nii”
%m：制造商名称。 例如，“myName％m”的输出文件名将把来自GE扫描仪的图像转换为“myNameGE.nii”，而来自Philips的图像将变为“myNamePh.nii”，而Siemens将变为“myNameSi.nii”，否则制造商不可用（“myNameNA.nii”）。 （需要2015年或之后的dcm2nii版本）。
%n：插入受试者姓名（DICOM标签0010,0010）。例如，“myName％n”的输出文件名将把来自John Doe的图像转换为“myNameJohnDoe.nii”。如果您的参与者名称仅使用英文字母，则此选项最有效。对于其他欧洲语言，您可能会发现它进行一些基本转换（“Müller”将变成“Muller”）。对于非欧洲语言，您会发现此选项不满意。也许以后的版本可以支持DICOM标签0008,0005。
%p：插入协议名称（DICOM标签0018,1030）。例如，“myName％p”的输出文件名将把协议命名为T1的图像转换为“myNameT1.nii”
%q：插入序列名称（DICOM标签0018,1020）。例如，使用输出文件名“myName％q”将旋转回波序列转换为“myNameSE.nii”（新功能，在2015年8月30日版本中）。
%s：插入系列（DICOM标签0020,0011）。例如，使用输出文件名“myName％s”将第二个序列转换为“myName2.nii”。如果您想将系列号补零，请插入所需的数字数（0..9）。例如，在转换11个序列时应用过滤器“m％s”将创建文件，这些文件将导致简单的按字母排序出现问题，例如“m1.nii，m11.nii，m2.nii...m9.nii”的区别在于指定“m％3s”将有助于排序（例如“m001.nii，m002.nii...m011.nii”）。
%t：插入会话日期和时间（DICOM标签0008,0021和0008,0030）。例如，“myName％t”的输出文件名将把会话开始于2014年1月13日下午1:23的图像转换为“myName20140113132322.nii”
%z：插入序列名称（0018,0024），因此使用“myName％z”转换的T1扫描可能会产生“myNameT1”。
1.-h 显示帮助屏幕
2.-m: 合并2D切片：（n/y or 0/1/2, default 2) [no, yes, auto]）如果选择，同一系列的图像将堆叠到单个NIfTI图像中. 默认就好了，3维数据直接在同一个 nii 里面。
3.-o: 输出文件夹（不给，就会直接放在input folder）
4.-z: 是否压缩，(y/o/i/n/3, default n) [y=pigz, o=optimal pigz, i=internal:zlib, n=no, 3=no,3D] 一般会选择压缩（-z y）
参数很多，但常用的转换命令如下（至少满足我的需求） dcm2niix -z y -f %i_%d_%s -o niftidir dcmdir

表示将 dcmdir 的所有图像转换到 niftidir 并压缩图像，重命名为 %i_%d_%s

dcm2nii小白教程网站
https://zhuanlan.zhihu.com/p/638003681
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
