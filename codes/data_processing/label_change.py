"""
    将type不为plate的xml文件，修改为type = plate
"""

import os

input_dir='D:/study/shixun/datasets/ourdatasets/Annotations/'
shu=0

import xml.etree.ElementTree as ET
for filename in os.listdir(input_dir):
    file_path = os.path.join(input_dir, filename)
    dom = ET.parse(file_path)
    root = dom.getroot()
    for obj in root.iter('object'):  # 获取object节点中的name子节点
        if obj.find('name').text != 'plate':
            obj.find('name').text= "plate"
            shu=shu+1

  # 保存到指定文件
    dom.write(file_path, xml_declaration=True)
print("有%d个文件被成功修改。" % shu)
