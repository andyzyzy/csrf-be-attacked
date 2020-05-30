#!/usr/bin/env python
# coding: utf-8
# Date  : 2020/5/30
# Author: zhangyi 
# Email : 450245556@qq.com
from flask import Flask, render_template, make_response, redirect, request, url_for

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':  # 取到表单中提交上来的参数
        username = request.form.get('username')
        password = request.form.get('password')
        if username and password:
            return render_template('/transfer.html')
    return render_template('/login.html')


@app.route('/transfer', methods=['POST', 'GET'])
def transfer():  # 从cookie中取到用户名
    to_account = request.form.get('to_account')
    print(to_account)
    # 如果没有取到，代表没有登录
    if not to_account:
        return redirect(url_for('index'))
    return "<html>转账成功</html>"


if __name__ == '__main__':
    app.run(debug=True, port=9000)
