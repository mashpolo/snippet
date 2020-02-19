#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from datetime import timedelta


basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False

    ###SQLALCHEMY
    SQLALCHEMY_POOL_SIZE = 6  # 数据库连接池的大小
    SQLALCHEMY_POOL_TIMEOUT = 30  # 指定数据库连接池的超时时间
    SQLALCHEMY_MAX_OVERFLOW = 2  # 控制在连接池达到最大值后可以创建的连接数。当这些额外的 连接回收到连接池后将会被断开和抛弃。
    SQLALCHEMY_POOL_RECYCLE = 28800  # 自动回收连接的秒数,8*60*60,超过8小时没用操作就自动断开连接
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False

    ###日志文件
    LOGFILE_DIR = "/tmp"
    LOGFILE_NAME = "phenas-deploy.log"
    LOGFILE_OPER_NAME = "daemon.oper.log"
    LOGFILE_ERROR_NAME = "daemon.error.log"

    # celery
    CELERY_IMPORTS = ('app.celerys.test_time', )

    CELERYBEAT_SCHEDULE = {
        'chk_app_status': {
            'task': 'app.celerys.test_time.chk_app_status',
            'schedule': timedelta(seconds=300)
        },
    }
    
    @staticmethod
    def init_app(app):
        pass


class ProductionConfig(Config):
    DEBUG = False


class TestingConfig(Config):
    DEBUG = True


class DevelopmentConfig(TestingConfig):
    DEBUG = True

    ###如果设置成 True，SQLAlchemy 将会记录所有 发到标准输出(stderr)的语句，这对调试很有帮助。
    SQLALCHEMY_ECHO = False
    MAIL_RECIPIENTS = ""

    # Celery配置
    CELERY_BROKER_URL = 'redis://127.0.0.1:6379'
    CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379'
    ### sso,celery,cache redis
    REDIS_CFG = {"host": "127.0.0.1", "port": 6379}

    ### jump mysql config
    JUMP_MYSQL_CFG = {"host": "127.0.0.1", "port": 3306,
                      "db": "test1", "user": "admin", "passwd": "admin123",
                      "charset": "utf8"}

    ### dop mysql config
    MAIN_MYSQL_CFG = {"host": "127.0.0.1", "port": 3306,
                     "db": "test2", "user": "admin", "passwd": "admin123"}
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{user}:{passwd}@{host}:{port}/{db}'.format(**MAIN_MYSQL_CFG)


config_env = {
    'production': ProductionConfig,
    'testing': TestingConfig,
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}



