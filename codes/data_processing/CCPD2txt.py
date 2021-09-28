"""
    从CCPD图片名中获取bbox标注信息，并写入txt
    获取的标注信息bbox = [x1, y1, x2, y2]
"""

import os
import cv2 as cv

def getbox_from_imgname(img_name):
    bbox = []

    name = img_name.split('.')[0]
    box = name.split('-')[2]

    # --- 边界框信息
    box = box.split('_')
    for i in box:
        bbox.append(int(i.split('&')[0]))
        bbox.append(int(i.split('&')[1]))
    # print(bbox)

    return bbox

def writetxt(bbox, img_name, txt_path):

    name = img_name.split('.')[0]
    with open(txt_path + name + ".txt", "w") as f:
        f.write("0" + " ")
        for i in bbox:
            f.write(str(i) + " ")


if __name__ == '__main__':
    img_path = r'D:/study/shixun/datasets/CCPD2019/ours/'  # img路径
    txt_path = "D:/study/shixun/datasets/txt_test2/"

    IMG = os.listdir(img_path)
    for img_name in IMG:
        bbox = getbox_from_imgname(img_name)
        writetxt(bbox, img_name, txt_path)

    print("Finish!")