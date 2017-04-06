#!/usr/bin/env python
"""test cairo.ImageSurface.create_for_data() with a numpy array
"""

import cairo
import numpy

dir_ = "/tmp/"
imgW, imgH = 255, 255
data = numpy.ndarray (shape=(imgH,imgW,4), dtype=numpy.uint8)

for x in range(imgW):
    for y in range(imgH):
        alpha = y

        # cairo.FORMAT_ARGB32 uses pre-multiplied alpha
        data[y][x][0] = int(x * alpha/255.0)
        data[y][x][1] = int(y * alpha/255.0)
        data[y][x][2] = 0
        data[y][x][3] = alpha

stride = imgW * 4
surface = cairo.ImageSurface.create_for_data (data, cairo.FORMAT_ARGB32,
                                              imgW, imgH, stride)
ctx = cairo.Context (surface)
surface.write_to_png (dir_ + 'for_data2.png')