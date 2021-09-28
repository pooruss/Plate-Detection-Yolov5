# 数据介绍与代码使用说明



## Ⅰ 数据介绍

### 1.1 原始数据

#### 1.1.1 CCPD2019

​		CCPD数据集是中科大团队建立的车牌数据集，此数据集目标用于做端到端的目标检测训练，解决了传统车牌识别检测的数据集规模较小问题。该数据集是在安徽合肥市的停车场采集得来，采集时间从早上7：30到晚上10：00。数据采集人员手持Android POS机对停车场的车辆拍照并手工标注车牌位置。拍摄的车牌照片涉及多种复杂环境，包括模糊、倾斜、阴雨天、雪天等。总数据量约30W。

​		在datasets/all_datasets/中，**上传了CCPD2019样例**，如需查看所有数据集，可在此[下载地址](https://github.com/detectRecog/CCPD)下载

![image1](.\image\image1.png)

#### 1.1.2 bluegreenyello

​		CCPD2019数据集仅有蓝色车牌，本组成员从网上获取该数据集（包括了图片与xml标注信息），从而加入部分绿色车牌（204张）与黄色车牌（650张），扩充了蓝色车牌（882张），丰富了数据集。

​		在**datasets/all_datasets/**中，上传了bluegreenyello所有数据。



### 1.2 本项目所用数据集（our_datasets）

​		由于算力、时间等因素限制，难以训练30W+数据量的数据，于是对上述原始数据进行抽取整合工作。

​		**从CCPD2019每种图片类型中抽取十分之一**，获取约数据量3W的数据，并**加入所有bluegreenyello数据集**中的数据。同时注意到，尽管CCPD2019中有对车牌进行旋转处理，但旋转角度较小，以此训练的模型在遇到特殊情况下的竖直车牌时，可能表现不佳，于是对部分车牌进行大幅度旋转操作（约5000张），进行数据增强。**旋转图片加入our_datasets**中，组成最终的项目所用数据集our_datasets，共计约4W张图片。

​		在**datasets/our_datasets/**中，上传了训练所用的图片数据与对应的xml标注文件。



## Ⅱ 代码使用说明

### 2.1 data_processing

​		本项目所用模型为yolov5模型，需要voc类型数据，bluegreenyello数据集包含了图片与对应xml信息，但CCPD2019中仅含图片，且标注信息蕴含在图片名称中（例如025-95_113-154&383_386&473-386&473_177&454_154&383_363&402-0_0_22_27_27_33_16-37-15.jpg，bbox的左上，右下坐标为154&383_386&473），需要若干程序代码进行后续处理。

​		在**code/data_processing/**中，上传了数据处理所需的所有py文件。

​		**traversal.py：**遍历原始CCPD2019数据中的每一类型，随机取出1/10组成训练数据。

​		**CCPD2txt.py：**提取出图片名称中的bbox标注信息，生成对应的txt标注文件。

​		**rotate.py：**旋转图片，并生成旋转后的bbox标注信息，保存在对应txt文件中。

​		**txt2xml：**将生成的txt标注文件转化为xml标注文件。

​		**label_change：**检测xml中图片的标注type，修改所有type为“plate”。

​		**delect_xml_and_img：**删除产生某些错误的xml文件，并删除对应的img。

​		**rename_for_jpg_and_xml：**可修改img与xml图片名称。

​		**split_train_val：**划分数据集，生成训练、验证、测试集。

​		**voc_label.py：**从xml文件中读取图片type与box坐标，生成各数据对应的label，用于yolov5模型训练。



### 2.2 yolov5-master

​		在**code/yolov5-master/**中，上传了本项目训练所用的yolov5项目模型。**运行环境见requirements.txt**。

​		**train.py：**训练模型，内置参数可调。

​		**detect.py：**将训练的模型用于图片、视频车牌检测打码。修改需检测的图片、视频路径即可进行测试。

​		**utils/plot.py：**对输入的图像/视频定位目标检测框，将目标框内容用RGB（0，0，0）填充，即打上全黑的马赛克。

​		训练模型放置于code/yolov5-master/plate中，图片、视频测试结果位于code/yolov5-master/runs/detect中

<img src=".\image\image2.jpg" alt="image2" style="zoom:200%;" />

<img src=".\image\image3.jpg" alt="image3" style="zoom:200%;" />
