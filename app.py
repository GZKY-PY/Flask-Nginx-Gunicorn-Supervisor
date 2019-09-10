#encoding:utf-8

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'hello woody'

@app.route('/test/')
def test():
    return 'test'

@app.errorhandler(404) 
def page_not_found(error): 
    return 'sorry that is my 404'

if __name__ == "__main__":
    app.run(host="0.0.0.0")



'''
# 第一个app指的是app.py文件，第二个指的是flask应用的名字；

gunicorn -w 4 -b 0.0.0.0:8000 app:app (这是命令行启动)


# gunicorn.conf
# 并行工作进程数

workers = 4
# 指定每个工作者的线程数

threads = 2
# 监听内网端口5000

bind = '127.0.0.1:5000'
# 设置守护进程,将进程交给supervisor管理

daemon = 'false'
# 工作模式协程

worker_class = 'gevent'
# 设置最大并发量
worker_connections = 2000

# 设置进程文件目录
pidfile = '/var/run/gunicorn.pid'

# 设置访问日志和错误信息日志路径
accesslog = '/var/log/gunicorn_acess.log'
errorlog = '/var/log/gunicorn_error.log'

# 设置日志记录
loglevel = 'warning'


gunicorn -c gunicorn.conf app:app （以配置文件的方式启动）
此时如果是gunicorn.py实际上也是可以的

'''


