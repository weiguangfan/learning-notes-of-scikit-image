"""
读取和写入各种格式的图像的实用程序。

以下是可用的插件:

Plugin                                         Description

qt                                             使用Qt库快速显示图像。从0.18版本开始被废弃。将在0.20版本中被移除。

tifffile                                       使用tifffile.py加载和保存TIFF和基于TIFF的图像。

simpleitk                                      通过SimpleITK读取和写入图像

gdal                                           通过GDAL库（www.gdal.org）读取图像

fits                                           通过PyFITS读取FITS图像

imread                                         通过imread读取和写入图像

gtk                                            使用GTK库快速显示图像

pil                                            通过Python图像库读取图像

matplotlib                                     使用Matplotlib显示或保存图像

imageio                                        通过ImageIO库读取图像

"""