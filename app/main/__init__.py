# main 目录 : 包含主业务逻辑的路由和视图
# 操作:将 main 声明成一个蓝图应用
from flask import Blueprint
main = Blueprint('main',__name__)
from .import views