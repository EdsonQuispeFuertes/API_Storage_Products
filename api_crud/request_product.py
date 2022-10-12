"""This module contains the Product class."""
from abc import abstractmethod
from typing import Dict, Tuple, Any

from flask import jsonify, request, Flask
from api_crud.status_codes import StatusCode
from api_crud.request_base import Request
from execute_orm.orm_product import OrmProduct


class RequestProduct(Request):
    """This class is the APi Product."""

    def __init__(self, app: Flask, orm_product: OrmProduct) -> None:
        Request.__init__(self, app)
        self.__orm_product = orm_product

    @abstractmethod
    def get(self, identifier: str) -> Any:
        """This method is the action of the get request.
        if the identifier is true
        It is verified if the product entered is found.
        returning a product plus a status code message.
        otherwise it returns a message plus a status code."""
        if identifier:
            product = self.__orm_product.get_product(identifier)
            if product:
                return jsonify({'product': product}), StatusCode.OK.value
        else:
            products = self.__orm_product.get_products()
            if products:
                return jsonify(products), StatusCode.OK.value
        return jsonify(
            {'message': 'Product not found'}), StatusCode.NOT_FOUND.value

    @abstractmethod
    def post(self):
        """This method is the action of the subsequent request.
        It is verified if the product entered is found,
        If the product entered is true, a new product is registered.
        and return a message and status code."""
        if self.__orm_product.create_product(request.json):
            return jsonify({'message': 'Product registered successfully.'}), \
                   StatusCode.CREATED.value
        return jsonify({'message': 'The product could not be registered.'}), \
            StatusCode.BAD_REQUEST.value

    def register_route(self) -> None:

        """This method records the routes of the http methods."""
        view_func = RequestProduct.as_view(
            'product', self._app, self.__orm_product)
        self._app.add_url_rule('/product', methods=['POST'],
                               view_func=view_func)
        self._app.add_url_rule('/product/<string:identifier>', methods=['GET'],
                               view_func=view_func)
        self._app.add_url_rule('/product', methods=['GET'],
                               view_func=view_func,
                               defaults={'identifier': None})
