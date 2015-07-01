Science Aid
===========

## 主要模块

#### LeanRead 精益阅读

优秀的书籍, 需要精致的笔记

什么是精致的笔记?

1. 最初的阅读目的与收获
2. 还要再读一次么? 什么时间, 为什么?
3. 主线笔记. 核心思路与论据, 个人感悟评价
4. 精彩片段, 摘录.

#### FlatFile 扁平电子书管理

推荐手动维护 bookinfo 管理电子书信息.
rawname 存储首次上传所用的文件名,
若 bookinfo 为空, 则使用 rawname 作为展示的书名.

#### BookHub 图书信息管理

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
