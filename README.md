# Flask-Nginx-Gunicorn-Supervisor

sudo apt-get install nginx (如果本地有的话可忽略，kali就自带)

pip3 install flask, gunicorn, supervisor


A选择 直接启动app.py (默认5000端口) 

B选择 通过gunicorn配置文件启动(转发本地端口，自定义)

C选择 通过nginx配置文件启动(自定义的配置文件更加灵活)，常用

D选择 通过gunicorn + nginx启动项目(具体为啥要这么干可以google，这里就不说了)，就是这个demo啦

参考 https://www.cnblogs.com/xmxj0707/p/8452881.html

supervisor是个管理进程的库，有命令行 和 web界面


1 启动nginx (配置文件转发端口 和 gunicorn配置的端口一致)，可以单独启动，也可以用supervisor启动


2 启动gunicorn (通过supervisor启动)




启动nginx的几种方式
cd usr/local/nginx/sbin && ./nginx (默认启动)

/etc/init.d/nginx start (默认会读取default.conf配置文件,路径/etc/nginx/conf.d)


echo_supervisord_conf > supervisor.conf # 导出配置模板 (可以自定义路径，随意)

然后在supervisor.conf 添加内容来开启 gunicorn

启动命令 supervisord -c supervisor.conf


进入shell交互

supervisorctl -c ./supervisord.conf

更多详细信息见  http://www.ttlsa.com/linux/using-supervisor-control-program/




开机启动supervisor

vim /etc/rc.local (ubuntu)

#添加以下内容
supervisord -c path/supervisor.conf # path是supervisor.conf的路径

supervisorctl start all #启动所有的程序


开启服务:
  







