"""
    从CCPD2019每类数据中，各取1/10组成参与训练的数据集
"""

import shutil
import os
from random import shuffle
def mkdir(path):
    folder = os.path.exists(path)
    if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
        os.makedirs(path)  # makedirs 创建文件时如果路径不存在会创建这个路径
        print
        "---  new folder...  ---"
        print
        "---  OK  ---"
    else:
        print
        "---  There is this folder!  ---"

# path = '图片的上两层的文件夹路径，如D:\code\python\E\sample1\1.jpg, 则写D:\code\python\E\'
path = 'D:/study/shixun/datasets/CCPD2019/'

for root, dirs, files in os.walk(path):
    if root == path:
        continue
    brotherroot = path+"/"+"ours"
    mkdir(brotherroot)
    #if len(dirs) == 0:
    shuffle(files)
    for i in range(round(len(files)/10)):
        if files[i][-3:] == 'jpg':
            file_path = root + '/' + files[i]
            new_file_path = brotherroot + '/' + files[i]
            shutil.copyfile(file_path, new_file_path)

print("finish!")