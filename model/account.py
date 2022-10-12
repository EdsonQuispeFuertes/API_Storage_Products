"""This module contains the account base object."""
from typing import List, Any
from source_orm.orm_base_object import OrmBaseObject


class Account(OrmBaseObject):

    """This class is the account's model object."""

    def __init__(self) -> None:
        OrmBaseObject.__init__(self)
        self._username: str = ""
        self._password: str = ""
        self._id_user: int = 0
        self._id_role: int = 0

    def id_account(self) -> Any:
        """This method returns the account id."""
        return self._id

    def username(self) -> str:
        """This method returns the username."""
        return self._username

    def password(self) -> str:
        """This method returns the password."""
        return self._password

    def role(self) -> int:
        """This method returns the role."""
        return self._id_role

    def id_user(self) -> int:
        """This method returns the id user."""
        return self._id_user

    def load_attributes(self, list_arguments: List[Any]) -> None:
        """This method loads its value to the attributes,
        using an order with the indexes of a list.
        That list is received as a parameter."""
        if isinstance(list_arguments, list):
            self._id = list_arguments[0]
            self._username = list_arguments[1]
            self._password = list_arguments[2]
            self._id_user = list_arguments[3]
            self._id_role = list_arguments[4]
        elif isinstance(list_arguments, dict):
            self._id = list_arguments["id"]
            self._username = list_arguments["username"]
            self._password = list_arguments["password"]
            self._id_user = list_arguments["id_user"]
            self._id_role = list_arguments["id_role"]
