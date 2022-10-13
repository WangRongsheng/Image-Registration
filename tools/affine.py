'''
$ git clone https://github.com/SuperElastix/SimpleElastix
$ mkdir build
$ cd build
$ cmake ../SuperBuild
$ make -j4
$ cd SimpleITK-build/Wrapping/Python
$ python Packaging/setup.py install
'''

import SimpleITK as sitk

elastixImageFilter = sitk.ElastixImageFilter()
elastixImageFilter.SetFixedImage(sitk.ReadImage("./test_png/200.png",sitk.sitkUInt8))
elastixImageFilter.SetMovingImage(sitk.ReadImage("./test_png/201.png",sitk.sitkUInt8))
elastixImageFilter.SetParameterMap(sitk.GetDefaultParameterMap("affine"))
elastixImageFilter.Execute()
#sitk.WriteImage(elastixImageFilter.GetResultImage())
#sitk.WriteImage(elastixImageFilter.GetResultImage(), 'result.nii')
#sitk.WriteImage(elastixImageFilter.GetResultImage(), 'result.png')
#sitk.WriteImage(sitk.Cast(elastixImageFilter.GetResultImage(),sitk.sitkFloat32),"affine_result.png")
sitk.WriteImage(sitk.Cast(elastixImageFilter.GetResultImage(),sitk.sitkUInt8),"affine_result.png")