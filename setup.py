#! /usr/bin/env python
# -*- coding: utf-8 -*_
from distutils.core import setup
import setuptools

setup(
    name='acv',  # 包的名字
    version='1.0',  # 版本号
    description='project describe',  # 描述
    author='George',  # 作者
    author_email='xxx@qq.com',  # 你的邮箱**
    url='https://github.com/rush9838465/acv',  # 可以写github上的地址，或者其他地址
    packages=setuptools.find_packages(),  # 包内不需要引用的文件夹

    # 依赖包
    install_requires=[
        'numpy',
        'opencv-python',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: Microsoft'  # 你的操作系统
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',  # BSD认证
        'Programming Language :: Python',  # 支持的语言
        'Programming Language :: Python :: 3',  # python版本 。。。
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        'Topic :: Software Development :: Libraries'
    ],
    zip_safe=True,
)