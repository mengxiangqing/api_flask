#!/usr/bin/env python  
# encoding: utf-8  


USERNAME = 'root'
PASSWORD = '135790'
HOSTNAME = "127.0.0.1"
PORT = '3306'
DATABASE = 'flask'

DIALECT = 'mysql'
DRIVER = 'pymysql'

# 连接数据的URI
DB_URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(DIALECT, DRIVER, USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)

SQLALCHEMY_DATABASE_URI = DB_URI

SQLALCHEMY_TRACK_MODIFICATIONS = True

SWAGGER_TITLE = "API"
SWAGGER_DESC = "API接口"
# 地址，必须带上端口号
SWAGGER_HOST = "10.190.0.30:2580"
