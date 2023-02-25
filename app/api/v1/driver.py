from app.libs.error_code import SearchSuccess, CreateSuccess
from app.libs.red_print import RedPrint
from app.model.driver import Driver

api = RedPrint('driver')


@api.route('', methods=['GET'])
def get_drivers_api():
    return SearchSuccess(data=Driver.search_all())


@api.route('', methods=['POST'])
def create_driver_api():
    from app.validator.driver import DriverForm
    data = DriverForm().validate_for_api().data_
    Driver.create(**data)
    return CreateSuccess()
