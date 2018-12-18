#只处理与users相关的业务
from . import users

@users.route('/users/index')
def users_index():
    return "这是users中的首页"