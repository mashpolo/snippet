#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import multiprocessing

bind = '0.0.0.0:8006'   #绑定的ip及端口号
backlog = 512                #监听队列
# worker_class = "gevent"     #使用gevent模式，还可以使用sync 模式，默认的是sync模式
chdir = '/opt/daemon/app'  #你项目的根目录,比如我的app.py文件在/home/ubuntu/app目录下，就填写'/home/ubuntu/app'
timeout = 90      #超时
proc_name = 'daemon.gunicorn.proc'
workers = 1   #进程数

loglevel = 'info' #日志级别，这个日志级别指的是错误日志的级别，而访问日志的级别无法设置
access_log_format = '%(t)s %(p)s %(h)s "%(r)s" %(s)s %(L)s %(b)s %(f)s" "%(a)s"'    #设置gunicorn访问日志格式，错误日志无法设置
accesslog = "/tmp/daemon.gunicorn.access.log"      #访问日志文件
errorlog = "/tmp/daemon.gunicorn.error.log"        #错误日志文件
