1、python版本
python 3.6.4
runserver --host=0.0.0.0 --port=8008
celery -A -A run.celery worker -B -l info
