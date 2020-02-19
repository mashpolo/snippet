#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from app import create_app, make_celery
from flask_script import Manager
from flask_apscheduler import APScheduler
from flask_migrate import Migrate, MigrateCommand

from app.schl.jobs import JOBS

app = create_app(os.getenv('FLASK_ENV') or 'default')
celery = make_celery(app)
from app import db
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

app.config.update(JOBS=JOBS)
scheduler = APScheduler()
scheduler.init_app(app)
scheduler.start()


if __name__ == '__main__':
    from werkzeug.contrib.fixers import ProxyFix
    app.wsgi_app = ProxyFix(app.wsgi_app)
    manager.run()

