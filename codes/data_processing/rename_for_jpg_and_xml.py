"""
    重命名img与xml
"""

import os
xml_path = r'D:/study/shixun/datasets/ourdatasets/Annotations/'
img_path = r'D:/study/shixun/datasets/ourdatasets/JPEGImages/'
f = os.listdir(img_path)
n=0

import random
L1 = random.sample(range(0, 26439), 26438)

for i in f :
       num = str(n)
       oldname = i.split('.')[0]
       oldtype = i.split('.')[1]
       img_oldname = img_path + oldname + "." + 'jpg'
       xml_oldname = xml_path + oldname + '.XML'
       img_newname = img_path + num.zfill(6) + '.jpg'
       xml_newname = xml_path + num.zfill(6) + '.xml'

       os.rename(img_oldname, img_newname)

       print(img_oldname, '--->', img_newname)

       os.rename(xml_oldname, xml_newname)

       print(xml_oldname, '--->', xml_newname)
       n += 1



