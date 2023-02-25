import requests
import time
from flask_login import current_user, login_required, login_user, logout_user

from app.libs.error_code import DeleteSuccess, Success, SearchSuccess, ModifySuccess
from app.libs.red_print import RedPrint
from app.model.user import User
from app.model.commodity import Commodity
from app.model.purchase_history import Purchase_History
from app.validator.purchase_history import PurchaseHistoryForm


api = RedPrint('commodity')


@api.route('/get', methods=['GET'])
def get_commodity_api():
    commodities = Commodity.search_all()
    return SearchSuccess(data=commodities)


@api.route('/buy', methods=['POST'])
def buy_commodity_api():
    form = PurchaseHistoryForm().validate_for_api().data_
    content = form['content']

    car_id = form['car']

    for i in content:
        # 更新商品表
        commodity = Commodity.search(_car_id=car_id, _commodity_id=i[0])['data']
        for item in commodity:
            item.modify(remaining_num=item['remaining_num']-i[1])
        # 更新购买记录表
        new_history = Purchase_History.create()
        new_history.modify(car_id=car_id, username=form['username'], date=time.ctime(), commodity_id=i[0], num=i[1])
    return ModifySuccess('购买成功')



