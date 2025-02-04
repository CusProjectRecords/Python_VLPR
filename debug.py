# -*- coding: utf-8 -*-

import cv2
import numpy as np


# 用于中间环节对处理图像的输出

def img_show(filename):
    """
    显示指定名称的图片文件
    :param filename:
    :return:
    """
    if filename.dtype == "float32":
        filename = filename.astype(np.uint8)
    cv2.imshow("img_show", filename)
    cv2.waitKey(0)


def img_contours(oldimg, box):
    box = np.int0(box)
    oldimg = cv2.drawContours(oldimg, [box], 0, (0, 0, 255), 2)
    cv2.imshow("img_contours", oldimg)
    cv2.waitKey(0)


def img_car(img_contours):

    pic_hight, pic_width = img_contours.shape[:2]
    return pic_hight, pic_width
