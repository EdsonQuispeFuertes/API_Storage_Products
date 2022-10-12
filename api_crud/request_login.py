"""This module contains the Login controller class."""
from abc import abstractmethod
from typing import Tuple, Dict

from flask import jsonify, request, Flask

from api_crud.request_base import Request
from api_crud.status_codes import StatusCode, AccountStatus
from execute_orm.orm_login import OrmLogin


class RequestLogin(Request):
    """This class is the APi login controller."""

    def __init__(self, app: Flask, orm_login: OrmLogin):
        Request.__init__(self, app)
        self.__orm_login = orm_login

    @abstractmethod
    def post(self):
        """This method is the action of the post request.
        It is verified if the account entered is found,
        if the account is registered,
        all the data of that account is returned plus a status code;
        otherwise, it returns a message and a status code."""
        account = self.__orm_login.get_account(request.json)
        if account:
            return jsonify(account), StatusCode.OK.value
        return jsonify(
            {'message': 'Account not found'}), StatusCode.NOT_FOUND.value

    def register_route(self) -> None:
        """This method records the routes of the http methods."""
        view_func = RequestLogin.as_view(
            'login', self._app, self.__orm_login)
        self._app.add_url_rule(
            '/login', view_func=view_func, methods=['POST'])
