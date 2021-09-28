"""
    删除存在异常的xml文件与对应的image
"""

import os
import xml.etree.ElementTree as ET

# 删除xml
xml_path = r'D:/study/shixun/datasets/ourdatasets/Annotations/'
XML = os.listdir(xml_path)
count = 0
qxml_list = []
for xml in XML:
    in_file = open('D:/study/shixun/datasets/ourdatasets/Annotations/' + xml, encoding='UTF-8')
    tree = ET.parse(in_file)
    root = tree.getroot()
    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)

    object = root.find('object')
    xmlbox = object.find('bndbox')
    xmin = xmlbox.find('xmin').text
    xmax = xmlbox.find('xmax').text
    ymin = xmlbox.find('ymin').text
    ymax = xmlbox.find('ymax').text
    if w == 0 or h == 0:
        # print((w, h))
        # print(xml)
        count += 1
        qxml_list.append(xml)
    if '-' in xmin or '-' in xmax or '-' in ymin or '-' in ymax or '_' in xmin or \
        '_' in xmax or '_' in ymin or '_' in ymax:
        count += 1
        qxml_list.append(xml)
for xml in qxml_list:
    os.remove("D:/study/shixun/datasets/ourdatasets/Annotations/" + xml)
print('total = ', count)


#删除xml对应的image
img_path = r'D:/study/shixun/datasets/ourdatasets/JPEGImages/'  # img路径

XML = os.listdir(xml_path)
IMG = os.listdir(img_path)

xml_number_list = []
for xml in XML:
       xml_number = xml.split('.')[0]
       xml_number_list.append(xml_number)

for img in IMG:
       img_number = img.split('.')[0]
       if img_number not in xml_number_list:
           os.remove('D:/study/shixun/datasets/ourdatasets/JPEGImages/' + img)

print("Finish!")