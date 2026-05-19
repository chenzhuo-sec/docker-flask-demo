# Docker Flask 电商商品列表示例

## 项目简介
这是一个基于 **Flask + Docker** 的电商商品列表网页示例项目，演示了：

- Flask 后端 API 服务
- 动态生成商品列表 JSON 数据
- 前端网页渲染商品卡片（HTML + CSS + JS）
- Docker 容器化部署
- 可通过 Docker Compose 一键启动


---

## 功能特点

1. 首页网页展示电商商品列表  
2. 点击刷新按钮获取最新商品列表（从 `/api/products` API）  
3. 每个商品卡片包含：图片、名称、价格  
4. 使用 Docker 容器化，方便本地或云端部署  
5. 结构清晰，易于扩展，例如添加购物车、搜索、数据库等功能  

---

## 项目结构

```text
docker-flask-demo/
├── app.py                  # Flask 后端主程序
├── requirements.txt        # Python 依赖
├── Dockerfile              # Docker 镜像构建
├── docker-compose.yml      # Docker Compose 一键部署
├── templates/
│   └── index.html          # 网页模板
├── static/
│   ├── style.css           # CSS 样式
│   └── script.js           # 前端 JS 脚本
│   └──images
├── .dockerignore
├── .gitignore
└── README.md
```

## 本地运行

1. 使用 Docker Compose 一键启动
Bash

docker compose up --build
2. 访问网页
在浏览器打开：


http://localhost:5000
首页显示商品列表网页

点击 “刷新商品列表” 按钮可以重新获取最新商品数据

3. 停止服务
Bash

docker compose down

## **Docker 镜像说明**

基础镜像：python:3.11-slim

安装依赖：requirements.txt

暴露端口：5000

容器运行命令：python app.py

API 接口
GET /api/products
返回 JSON 格式的商品列表：

JSON

[
    {"id": 1, "name": "智能手表", "price": 399, "image": "/static/images/watch.png"},
    {"id": 2, "name": "蓝牙耳机", "price": 299, "image": "/static/images/earphone.png"},
    ...
]

## 技术栈

Python 3 + Flask

HTML / CSS / JS 前端

Docker + Docker Compose 容器化部署
