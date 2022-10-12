"""This module contains the orm login class."""
from typing import Dict, Any

from orm import Orm

from model.account import Account
from model.users import Users


class OrmLogin:
    """This class is the orm login."""

    def __init__(self, orm: Orm):
        self.__orm = orm

    def get_account(
            self, data: Dict[str, str])\
            -> Dict[str, Dict[str, Any]]:
        """This method verifies if an account exists in the database,
        if it exists, it returns all the data of that account,
        otherwise, it returns a False."""
        self.__orm.set_conditional_where_select('and')
        account = self.__orm.search_objects(
            Account(), {"username": data["username"],
                        "password": data["password"]})
        if account:
            user = self.__orm.search_objects(
                Users(), {"id": account[0].__dict__["_id_user"]})
            return {"account": account[0].__dict__,
                    "user": user[0].__dict__}
        return {}

    def get_orm(self) -> Orm:
        """This method returns the orm."""
        return self.__orm
