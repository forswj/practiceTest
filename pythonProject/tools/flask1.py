# from flask import app
from flask import Flask, request, render_template

app = Flask(__name__)


# @app.route('/api/login', methods=['post'])
# def first_flask():
#     return "hello flask"

@app.route('/api/loging', methods=['post', 'get'])
def login():
    return render_template('index.html')


if __name__ == '__main__':
    # 启动服务 debug=True代表实时更新
    app.run(debug=False)
