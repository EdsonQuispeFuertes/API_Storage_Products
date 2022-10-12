"""This module contains the user base object."""
from typing import List, Any

from source_orm.orm_base_object import OrmBaseObject


class Users(OrmBaseObject):
    """This class is the user's model object."""

    def __init__(self) -> None:
        OrmBaseObject.__init__(self)
        self._first_name: str = ""
        self._last_name: str = ""
        self._identity_card: int = 0
        self._phone: int = 0
        self._email: str = ""
        self._birthday: str = ""

    def id_user(self) -> Any:
        """This method returns the user id."""
        return self._id

    def name(self) -> str:
        """This method returns the name."""
        return self._first_name

    def first_last_name(self) -> str:
        """This method returns the first last name."""
        return self._last_name

    def identity_card(self) -> int:
        """This method returns the identity card."""
        return self._identity_card

    def phone(self) -> int:
        """This method returns the phone."""
        return self._phone

    def email(self) -> str:
        """This method returns the email."""
        return self._email

    def birthday(self) -> str:
        """This method returns the birthday."""
        return self._birthday

    def load_attributes(self, list_arguments: List[Any]) -> None:
        """This method loads its value to the attributes,
        using an order with the indexes of a list.
        That list is received as a parameter."""
        if isinstance(list_arguments, list):
            self._id = list_arguments[0]
            self._first_name = list_arguments[1]
            self._last_name = list_arguments[2]
            self._identity_card = list_arguments[3]
            self._phone = list_arguments[4]
            self._email = list_arguments[5]
            self._birthday = list_arguments[6]
        elif isinstance(list_arguments, dict):
            self._id = list_arguments.get("id")
            self._first_name = list_arguments.get("first_name")
            self._last_name = list_arguments.get("last_name")
            self._identity_card = list_arguments.get("identity_card")
            self._phone = list_arguments.get("phone")
            self._email = list_arguments.get("email")
            self._birthday = list_arguments.get("birthday")
