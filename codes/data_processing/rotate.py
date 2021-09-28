"""
    实现图片和bbox的旋转操作，生成旋转图片与对应的txt
    本次旋转角度设置为90°
"""
import os
import cv2 as cv
import numpy as np
import math
from PIL import Image
from CCPD2txt import getbox_from_imgname, writetxt

def rotate_img(image, angle):
    """
    :param image: 图片名
    :param image: 旋转角度（90°）
    :return: 旋转后的bbox
    """
    # grab the dimensions of the image and then determine the
    # center
    (h, w) = image.shape[:2]
    (cX, cY) = (w // 2, h // 2)

    # grab the rotation matrix (applying the negative of the
    # angle to rotate clockwise), then grab the sine and cosine
    # (i.e., the rotation components of the matrix)
    M = cv.getRotationMatrix2D((cX, cY), -angle, 1.0)
    cos = np.abs(M[0, 0])
    sin = np.abs(M[0, 1])

    # compute the new bounding dimensions of the image
    nW = int((h * sin) + (w * cos))
    nH = int((h * cos) + (w * sin)) #返回长宽

    # adjust the rotation matrix to take into account translation
    M[0, 2] += (nW / 2) - cX
    M[1, 2] += (nH / 2) - cY

    # print(nW, nH)
    # 将周围背景设置为紫色
    return cv.warpAffine(image, M, (nW, nH), borderValue=(128, 0 ,128))

def rotate_box(angle, box, img):
    """
    :param angle: 旋转角度（90°）
    :param box:  [int(j) for j in i[2:6]] 四个数值的列表，表示 x1,y1,x2,y2
    :param img：图片名
    :return: 旋转后的bbox
    """
    angle = angle % 360.0

    img = Image.fromarray(np.uint8(img))

    h = img.size[1]
    w = img.size[0]
    center_x = int(np.floor(w / 2))
    center_y = int(np.floor(h / 2))
    # print('center_x,center_y', center_x, center_y)

    angle_pi = math.radians(angle)  # 转化为弧度角度

    # 计算某个点绕坐标轴原点中心旋转后的坐标
    def transform(x, y): # angle 必须是弧度
        return (x - center_x) * round(math.cos(angle_pi), 15) + \
               (y - center_y) * round(math.sin(angle_pi), 15) + center_x, \
              -(x - center_x) * round(math.sin(angle_pi), 15) + \
               (y - center_y) * round(math.cos(angle_pi), 15) + center_y

    # 通过四个顶点的坐标变化后的情况得出新的坐标系和原有坐标系的偏移量dx,dy
    # 分为三种情况，w=h,dx,dy 都会一直为正
    # w>h, dx 会出现为负的情况
    # w<h, dy 会出现为负的情况
    xx = []
    yy = []
    for x, y in ((0, 0), (w, 0), (w, h), (0, h)):
        x_, y_ = transform(x, y)
        xx.append(int(x_))
        yy.append(int(y_))
    if min(xx) < 0:
        dx = abs(min(xx))
    else:
        dx = -abs(min(xx))
    if min(yy) < 0:
        dy = abs(min(yy))
    else:
        dy = - abs(min(yy))
    # print(angle, angle_pi, 'dx,dy', dx, dy, h, w, xx, yy)

    box_rot = []
    xx = []
    yy = []
    for x, y in ((box[0], box[1]),
                 (box[0], box[3]),
                 (box[2], box[1]),
                 (box[2], box[3])):
        x_, y_ = transform(x, y)
        xx.append(x_)
        yy.append(y_)
    box_rot.append([int(min(xx) + dx), int(min(yy) + dy),
                    int(max(xx) + dx), int(max(yy) + dy),
                   ])

    return box_rot[0]

if __name__ == '__main__':
    img_path = r'D:/study/shixun/datasets/CCPD2019/ours/'  # img路径
    txt_path = "D:/study/shixun/datasets/txt_rotate/"
    IMG = os.listdir(img_path)
    for img_name in IMG:
        image = cv.imread(img_path + img_name)
        img_rotate = rotate_img(image, 90)
        bbox = getbox_from_imgname(img_name)
        bbox_rotate = rotate_box(-90, bbox, image)

        cv.imwrite('D:/study/shixun/datasets/img_rotate/' + img_name, img_rotate)
        writetxt(bbox_rotate, img_name, txt_path)

    print("Finish!")



