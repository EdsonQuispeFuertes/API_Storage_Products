"""This module contains the User class."""
from flask import jsonify, request, Flask

from api_crud.status_codes import StatusCode
from api_crud.request_base import Request
from execute_orm.orm_user_register import OrmUserRegister


class RequestUser(Request):
    """This class is the APi User."""

    def __init__(self, app: Flask, orm_user: OrmUserRegister) -> None:
        Request.__init__(self, app)
        self.__orm_user = orm_user

    def post(self):
        """
        This method is the action of the subsequent request.
        It is verified if the user entered is found,
        If the user entered is true, a new user is registered.
        and return a message and status code.
        :return: Tuple[Dict[str, str], int]
        """
        if self.__orm_user.create_new_user(request.json):
            return jsonify({'message': 'User registered successfully.'}), \
                   StatusCode.CREATED.value
        return jsonify({'message': 'The user could not be registered.'}), \
            StatusCode.BAD_REQUEST.value

    def get(self, identifier: str):
        """This method is the action of the get request.
        if the identifier is true
        It is verified if the user entered is found.
        returning a user plus a status code message.
        otherwise it returns a message plus a status code."""
        if identifier:
            user = self.__orm_user.get_user(identifier)
            if user:
                return jsonify({'user': user}), StatusCode.OK.value
        else:
            users = self.__orm_user.get_all_user()
            if users:
                return jsonify(users), StatusCode.OK.value
        return jsonify(
            {'message': 'User not found'}), StatusCode.NOT_FOUND.value

    def put(self, identifier: str):
        """This method is in charge to update a user object."""
        res = {'Status': 'This method was not implemented'}
        return res, StatusCode.UNAUTHORIZED.value

    def delete(self, identifier: str):
        """This method is in charge to delete a user object."""
        res = {'Status': 'This method was not implemented'}
        return res, StatusCode.UNAUTHORIZED.value

    def register_route(self):
        """This method records the routes of the http
        methods in request user class."""
        view_func = RequestUser.as_view(
            'user', self._app, self.__orm_user)
        self._app.add_url_rule('/register', methods=['POST'],
                               view_func=view_func)
        self._app.add_url_rule('/user/<string:identifier>', methods=['GET'],
                               view_func=view_func)
        self._app.add_url_rule('/users', methods=['GET'],
                               view_func=view_func,
                               defaults={'identifier': None})
