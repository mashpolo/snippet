#!/usr/bin/env python
# -*- coding: utf-8 -*-
from concurrent.futures import ThreadPoolExecutor
from flask import Flask
from flask_cors import CORS
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from config import config_env

db = SQLAlchemy()
ma = Marshmallow()


def to_dict(self):
    return {c.name: getattr(self, c.name, None) for c in self.__table__.columns}


db.Model.to_dict = to_dict

mail = None
threadPool = ThreadPoolExecutor(max_workers=60)


def create_app(config_name):
    """
    初始化flask app
    :param config_name:
    :return:
    """
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config_env[config_name])
    CORS(app)
    db.init_app(app)
    
    global mail
    mail = Mail(app)
    
    ###注册蓝图
    from app.urls import register_app
    register_app(app)
    
    @app.teardown_request
    def teardown_request(exception=None):
        try:
            db.session.remove()
        except:
            pass
    
    return app


def make_celery(app):
    """
    初始化celery
    http://flask.pocoo.org/docs/1.0/patterns/celery/
    :param app:
    :return:
    """
    from celery import Celery
    celery = Celery(
        app.import_name,
        backend=app.config['CELERY_RESULT_BACKEND'],
        broker=app.config['CELERY_BROKER_URL']
    )
    celery.conf.update(app.config)
    
    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)
    
    celery.Task = ContextTask
    
    return celery
