#对整个应用做初始化操作
#主要工作
#1.构建Flask应用以及各种配置
#2.构建SQLAlchemy的应用

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql
pymysql.install_as_MySQLdb()

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    #配置启动模式为调试模式
    app.config['DEBUG']=True # app.run(debug=True)
    #配置数据库的连库字符串
    app.config['SQLALCHEMY_DATABASE_URI']="mysql://root:123456@localhost:3306/blog"
    #配置自动提交
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
    #配置SECRET_KEY ,SESSION时使用
    app.config['SECRET_KEY'] = 'aixieshaxiesha'
    #数据库应用实例的初始化
    db.init_app(app)

    #将main蓝图程序关联到app上
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    #将users蓝图程序关联到app上
    from .users import users as users_blueprint
    app.register_blueprint(users_blueprint)


    return app
