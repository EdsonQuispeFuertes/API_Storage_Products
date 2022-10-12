from flask import Flask
from flask_cors import CORS

from source_orm.functions_orm import get_parameters_file
from source_orm.sql_server_connection import SqlServerConnection
from source_orm.orm import Orm

from api_crud.request_login import RequestLogin
from execute_orm.orm_login import OrmLogin
from api_crud.request_product import RequestProduct
from execute_orm.orm_product import OrmProduct
from api_crud.request_user import RequestUser
from execute_orm.orm_user_register import OrmUserRegister
from api_crud.custom_json_encoder import CustomJSONEncoder


class Main:
    def __init__(self):
        self._app = Flask(__name__)
        self._app.json_encoder = CustomJSONEncoder
        CORS(self._app)
        parameters_connection = get_parameters_file("", "mysql")
        connection = SqlServerConnection(parameters_connection)
        orm = Orm(connection, 'mysql', "model")
        # Login
        orm_login = OrmLogin(orm)
        self.login_controller = RequestLogin(self._app, orm_login)
        # User
        orm_user = OrmUserRegister(orm)
        self.user = RequestUser(self._app, orm_user)
        # Product
        orm_product = OrmProduct(orm)
        self.product = RequestProduct(self._app, orm_product)

    def start(self):
        self.user.register_route()
        self.product.register_route()
        self.login_controller.register_route()
        self._app.run(host='localhost', debug=True, port=2000)


if __name__ == '__main__':
    run = Main()
    run.start()
