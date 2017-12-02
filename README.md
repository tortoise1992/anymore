# anymore
记录一下自己用python写web应用的过程

## 开发环境
python3.5,django1.11.2,mysql5.6

## 项目准备
1，创建一个名为ahuife的工程：django-admin startproject ahuife

2，在ahuife工程下，创建一个名为blog的app：
> 首先进入工程根目录：cd ahuife

> 然后在终端输入：python manage.py startapp blog

> django默认使用的数据库是sqllite3,我们需要手动将默认数据库改为mysql，找到settings.py的DATABASES，修改为：
```
'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'ahuife',
        'USER':'root',
        'PASSWORD':'123456',
        'HOST':'',
        'PORT':'3306',
        }
```
> 默认情况下，django是不支持mysql的，所以需要手动安装mysql驱动。对于3.5版本，windows系统下面，需要安装mysqlclient：pip install mysqlclient

## 常用命令

#### 1，同步数据库

（1）python manage.py makemigrations

（2）python manage.py migrate

#### 2，项目启动

python manage.py runserver 3000