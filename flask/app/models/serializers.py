#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2020-01-07

"""
import re

from marshmallow import fields, validate

from app import ma
from app.models.db import RegistryCenter


regex = '''^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.(
            25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.(
            25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.(
            25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)'''


class BaseSer(ma.ModelSchema):
    created = fields.DateTime(format='%Y-%m-%d %H:%M:%S')
    modified = fields.DateTime(format='%Y-%m-%d %H:%M:%S')


class RegeditSchema(BaseSer):
    project_code = fields.String(required=True)
    module_code = fields.String(required=True)
    ip = fields.String(required=True, validate=lambda ip: re.search(regex, ip))
    host_name = fields.String(required=True)
    instance_code = fields.String(required=True)
    group = fields.String()
    zone = fields.String()
    startup_time = fields.DateTime(required=True, format='%Y-%m-%d %H:%M:%S')
    create_token = fields.Boolean()
    tags = fields.String()
    http_port = fields.Integer()
    tcp_port = fields.Integer()
    monitor_port = fields.Integer()
    env_science = fields.String()
    token = fields.String()

    class Meta:
        model = RegistryCenter
        fields = ("project_code", "module_code", "ip", "host_name", "instance_code", "startup_time",
                  "group", "zone", "tags", "http_port", "tcp_port", "env_science", "monitor_port",
                  "token")
