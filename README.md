# acv
AI 常用的功能函数，包括数据集处理，数据增强等等

# install
pip install git+https://github.com/rush9838465/acv

# logs
2021/7/2: 

    添加数据增强：flip, rotation, hsv, crop, blur, brightness, contrast, resize and padding
    调用位置： acv.data_augmentation.transforms.py

    添加数据xml解析：解析xml到json格式；从xml中裁剪bbox; VOC数据集转yolov5格式
    调用位置： acv.datasets.xml_parsing.py

    添加excel解析：读写excel文件
    调用位置： acv.excel.base.py

2021/7/5:
    
    添加数据集加载（支持torch DataLoader）：VOC数据集格式

2021/7/26:
    
    添加优化器：余弦退火 SGD版本

2021/8/20:
    
    添加特征层可视化：feature_map_visualization.py
    功能介绍博客：
    https://blog.csdn.net/rush9838465/article/details/114291144

