# Image-Registration

## Tools工具类

- [convert_dcm2jpg.py](https://github.com/WangRongsheng/Image-Registration/blob/main/tools/convert_dcm2jpg.py) :读取dicom图像并且在三个维度上随意切割图片保存为jpg/png
- [dcm2nii.py](https://github.com/WangRongsheng/Image-Registration/blob/main/tools/dcm2nii.py) :dicom文件转化为nii文件，并且可以修改spacing、origin等
- [pydicom根据group获得tag的value.py](https://github.com/WangRongsheng/Image-Registration/blob/main/tools/pydicom%E6%A0%B9%E6%8D%AEgroup%E8%8E%B7%E5%BE%97tag%E7%9A%84value.py)
- [simitk显示某个slice的图像.py](https://github.com/WangRongsheng/Image-Registration/blob/main/tools/simitk%E6%98%BE%E7%A4%BA%E6%9F%90%E4%B8%AAslice%E7%9A%84%E5%9B%BE%E5%83%8F.py)
- [fix_spacing.py](https://github.com/WangRongsheng/Image-Registration/blob/main/tools/fix_spacing.py) ：修正dicom里面的spacing以及其他各种信息
- [affine.py](https://github.com/WangRongsheng/Image-Registration/blob/main/tools/affine.py) ：两张图像进行仿射配准，并保存为nii或者png格式
- [verify_affine.py](https://github.com/WangRongsheng/Image-Registration/blob/main/tools/verify_affine.py) ：根据上述affine.py产生的结果反向减法求出moving-image进行对比
