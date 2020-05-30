#!/usr/bin/env python
# coding: utf-8
# Date  : 2020/5/30
# Author: zhangyi 
# Email : 450245556@qq.com
from flask import Flask, render_template, make_response, redirect, request, url_for
from forms import TransferForm

app = Flask(__name__)
app.config['SECRET_KEY'] = "ANDY"

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':  # 取到表单中提交上来的参数
        username = request.form.get('username')
        password = request.form.get('password')
        if username and password:
            return redirect(url_for('transfer'))
    return render_template('/login.html')


@app.route('/transfer', methods=['POST', 'GET'])
def transfer():  # 从cookie中取到用户名
    form = TransferForm()
    # to_account = request.form.get('to_account')
    # 如果没有取到，代表没有登录
    if request.method == 'POST':
        return "<html>转账成功</html>" if form.validate_on_submit() else "<html>非法请求！！！！！</html>"
    return render_template('/transfer.html', form=form)


if __name__ == '__main__':
    app.run(debug=True, port=9000)
