#encoding:utf-8
import multiprocessing

from gevent import monkey
monkey.patch_all()

# 并行工作进程数
workers = multiprocessing.cpu_count() * 2 + 1

debug = True

reload = True # 自动重新加载

loglevel = 'debug'

# 指定每个工作者的线程数
threads = 2

# 转发为监听端口8000
bind = '0.0.0.0:5001'

# 设置守护进程,将进程交给supervisor管理
daemon = 'false'

# 工作模式协程
worker_class = 'gevent'

# 设置最大并发量
worker_connections = 2000

# 设置进程文件目录
pidfile = 'log/gunicorn.pid'
logfile = 'log/debug.log'

# 设置访问日志和错误信息日志路径
accesslog = 'log/gunicorn_acess.log'
errorlog = 'log/gunicorn_error.log'
