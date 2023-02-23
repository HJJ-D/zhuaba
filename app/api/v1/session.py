from flask_login import current_user, login_required, login_user, logout_user

from app.libs.error_code import DeleteSuccess, Success
from app.libs.red_print import RedPrint
from app.model.user import User

api = RedPrint('session')


@api.route('', methods=['GET'])
@login_required
def get_session_api():
    dic = set()
    return Success(data={
        'user': current_user,
        'permission': list(dic)
    })


@api.route('/<string:username>', methods=['POST'])
def create_session_api(username):
    user = User.get_by_id(username)
    if user is None:
        User.create(username=username)
        user = User.get_by_id(username)
    login_user(user, remember=True)
    return Success('登录成功')


@api.route('', methods=['DELETE'])
def delete_session_api():
    logout_user()
    return DeleteSuccess('登出成功')
