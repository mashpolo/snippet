# 操作
## python版本
- python 3.6.4 (celery4.2.x 仅支持python3.6)

## 执行命令
### 启动app
- python runserver --host=0.0.0.0 --port=8008

### 启动celery
- celery -A -A run.celery worker -B -l info
