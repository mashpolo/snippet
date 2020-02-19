#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2020-2-19

"""
from flask import Blueprint

main = Blueprint('main', __name__, url_prefix="/apis")


# 登录
@main.route('/login', methods=['POST'])
def hello():
    return 'hello, world'
