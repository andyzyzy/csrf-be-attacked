#!/usr/bin/env python
# coding: utf-8
# Date  : 2020/5/30
# Author: zhangyi 
# Email : 450245556@qq.com
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class TransferForm(FlaskForm):
    to_account = StringField(validators=[DataRequired(message='请输入名户名')])
    money = StringField(validators=[DataRequired(message='请输入密码')])
    submit = SubmitField('转账')
