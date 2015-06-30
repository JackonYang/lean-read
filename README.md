Science Aid
===========

## 关键功能点

从个性化学习做起

#### Flat File 电子书文件管理

推荐手动维护 bookinfo 管理电子书信息.
rawname 存储首次上传所用的文件名,
若 bookinfo 为空, 则使用 rawname 作为展示的书名.

#### Book Hub 图书信息管理

- 基本信息: 书名, 作者, 出版社
- 分类信息: tag, 分类
- 内容信息: 摘要, 目录


## Build Dev Env

```shell
# Prerequisites of Pillow on Ubuntu 14.04 LTS
# for more OS suport, go to http://pillow.readthedocs.org/en/latest/installation.html
$ sudo apt-get install libtiff5-dev libjpeg8-dev zlib1g-dev \
    libfreetype6-dev liblcms2-dev libwebp-dev tcl8.6-dev tk8.6-dev python-tk
$ sudo pip install -r requirement.txt
```
