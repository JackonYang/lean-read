## Code Map


#### 通用模块与框架

fixtures 目录下是该 app 的 model 的初始数据

- backup.sh  数据库与 media 目录下文件备份
- install.sh  数据库初始化, 加载默认数据
- run.sh  启动 runserver, 默认监听 8000 端口, 支持所有 IP 访问
- requirements.txt  开发环境依赖文件
- init\_data  初始化数据. media 目录下的图片, 视频等
- media:  资源文件, 主要是图片, 图像等
- static:  static root
- accounts:  用户管理, 帐号管理模块
- base:  project 基础模块.
    - settings.py  尝试在同目录下加载 local\_settings.py. 默认使用 sqlite3
    - wsgi.py  生产环境用 wsgi 部署
    - static/  通用静态文件
    - templates/
        - base.html  template 继承的 base
        - brand-logo.html  此处配置网站名, navbar.html 中用到
        - home.html  首页 content
        - navbar.html  导航栏
        - nav-list.html  导航栏的超链接. navbar.html 中用到
- docs:
    - code\_map.md  本文, 文档地图
    - frs/  需求管理
