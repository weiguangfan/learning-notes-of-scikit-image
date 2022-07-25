"""
skimage.io.imread(
                    fname,
                    as_gray=False,
                    plugin=None,
                    **plugin_args)
从文件中加载一个图像。

Parameters
    fname : string
            图片文件名，例如test.jpg或URL。

    as_gray : bool, optional
            如果为True，将彩色图像转换为灰度（64位浮点）。
            已经是灰度格式的图片不会被转换。

    plugin : str, optional
            要使用的插件的名称。
            默认情况下，会尝试不同的插件（从imageio开始），直到找到一个合适的候选插件。
            如果没有给定，并且fname是一个tiff文件，将使用tifffile插件。

Returns
    img_array : ndarray
                不同的色带/通道被存储在第三维中，例如，灰色图像是MxN，RGB图像是MxNx3，RGBA图像是MxNx4。

Other Parameters
    plugin_args : keywords
                传递给给定的插件。

"""
from skimage import io
io_imread = io.imread("../../../fish.JPEG")
print(io_imread)
