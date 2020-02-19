#!/usr/bin/env python
# -*- coding: utf-8 -*-

from app.apis.daemon import main


def register_app(app):
    app.register_blueprint(main)

