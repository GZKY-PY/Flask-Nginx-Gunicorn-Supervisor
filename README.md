# Flask-Nginx-Gunicorn-Supervisor

sudo apt-get install nginx (如果本地有的话可忽略，kali就自带)

pip3 install flask, gunicorn, supervisor


A选择 直接启动app.py (默认5000端口) 

B选择 通过gunicorn配置文件启动(转发本地端口，自定义)

C选择 通过nginx配置文件启动(自定义的配置文件更加灵活)，常用

D选择 通过gunicorn + nginx启动项目(具体为啥要这么干可以google，这里就不说了)，就是这个demo啦

supervisor是个管理进程的库，有命令行 和 web界面


1 启动nginx (配置文件转发端口 和 gunicorn配置的端口一致)，可以单独启动，也可以用supervisor启动
2 启动gunicorn (通过supervisor启动)





