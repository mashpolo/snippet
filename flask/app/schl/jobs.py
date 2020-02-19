#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2020-2-19

"""
from app.schl.schedule import chk_app_status

JOBS = [
    {
        'id': 'chk_app_status',
        'func': chk_app_status,
        'args': None,
        'trigger': 'interval',
        'seconds': 10
    }
]
