#!/usr/bin/env python  
# encoding: utf-8  

""" 
数据库映射
"""

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from exts import db
from api_app import app
from foo_models import Foo

# 显式写出要映射到数据库的模型




# 命令行封装app
manager = Manager(app)

# 绑定可以管理的数据库模型
migrate = Migrate(app,db)

# 加载数据库管理命令
manager.add_command("db",MigrateCommand)

if __name__ == '__main__':
    manager.run()



# 映射命令
# python3 manager.py db init
# python3 manager.py db migrate
# python3 manager.py db upgrade
