#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2020-2-19

"""
import os
from datetime import datetime, timedelta

from app import db
from app.models.db import RegistryCenter
from app import create_app
from config import config_env


def chk_app_status():
    # 获取环境变量
    print("====started=====")
    # env = os.getenv('FLASK_ENV', 'default')
    # # 创建app
    # app = create_app(config_env[env])
    # chk_time = (datetime.now() - timedelta(minutes=5))
    # try:
    #     with app.app_context():
    #         db.session.query(RegistryCenter). \
    #             filter(RegistryCenter.heartbeat_time < chk_time,
    #                    RegistryCenter.status == 0). \
    #             update({RegistryCenter.status: 1})
    #         db.session.commit()
    # except Exception as ex:
    #     db.session.rollback()
