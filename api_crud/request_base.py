"""This module contains the api base class."""
from abc import abstractmethod
from typing import Dict, Tuple

from flask import Flask
from flask.views import MethodView


class Request(MethodView):
    """This class is the basis of the api."""

    def __init__(self, app: Flask) -> None:
        self._app = app

    @abstractmethod
    def get(self, identifier: str) -> Tuple[Dict[str, str], int]:
        """This method is the action of the get request."""

    @abstractmethod
    def post(self) -> Tuple[Dict[str, str], int]:
        """This method is the action of the post request."""

    @abstractmethod
    def put(self, identifier: str) -> Tuple[Dict[str, str], int]:
        """This method is the action of the put request."""

    @abstractmethod
    def delete(self, identifier: str) -> Tuple[Dict[str, str], int]:
        """This method is the action of the delete request."""

    @abstractmethod
    def register_route(self) -> None:
        """This method records the route according to the http method."""
