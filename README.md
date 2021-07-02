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
    