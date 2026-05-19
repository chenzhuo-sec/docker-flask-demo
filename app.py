from flask import Flask, jsonify, render_template

app = Flask(__name__)

# 模拟商品列表数据
products = [
    {"id": 1, "name": "智能手表", "price": 399, "image": "/static/images/watch.png"},
    {"id": 2, "name": "蓝牙耳机", "price": 299, "image": "/static/images/earphone.png"},
    {"id": 3, "name": "无线键盘", "price": 149, "image": "/static/images/keyboard.png"},
    {"id": 4, "name": "笔记本电脑", "price": 5999, "image": "/static/images/laptop.png"}
]


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/products")
def get_products():
    return jsonify(products)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
