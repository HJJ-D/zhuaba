import requests
from flask_login import current_user, login_required, login_user, logout_user

from app.libs.error_code import DeleteSuccess, Success
from app.libs.red_print import RedPrint

api = RedPrint('session')


@api.route('', methods=['GET'])
@login_required
def get_session_api():
    dic = set()
    return Success(data={
        'user': current_user,
        'permission': list(dic)
    })


@api.route('/<string:code>', methods=['POST'])
def create_session_api(code):
    data = {
        'appid': 'wx9b353c6548c44f15',
        'secret': 'e4b56652625f23d64690171141fa5276',
        'js_code': code
    }
    r = requests.get('https://api.weixin.qq.com/sns/jscode2session', params=data)
    ans = r.json()
    user = User.get_by_id(ans['openid'])
    if user is None:
        User.create(username=ans['openid'])
        user = User.get_by_id(ans['openid'])
    login_user(user, remember=True)
    return Success('登录成功')


@api.route('', methods=['DELETE'])
def delete_session_api():
    logout_user()
    return DeleteSuccess('登出成功')
