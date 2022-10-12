"""This module contains the orm user class."""
from typing import Dict, Union, Any, List
from orm import Orm
from model.account import Account
from model.users import Users


class OrmUserRegister:
    """This class is the orm user."""

    def __init__(self, orm: Orm):
        self.__orm = orm

    def create_new_user(self, user: Dict[str, str]) -> bool:
        """
        This method creates a new user.
        First it is verified if the user is already registered,
        If the user already exists, it returns false.
        If the user does not exist,
        a new user is created with the dictionary entered.
        Then it returns true.
        :param user: Dict[str, str]
        :return: bool
        """
        if self.__orm.search_objects(
                Account(), {"username": user["first_name"]}):
            return False

        new_user = Users()
        new_user.load_attributes([0, user["first_name"],
                                  user["last_name"],
                                  user["identity_card"],
                                  user["phone"],
                                  user["email"],
                                  user["birthday"]])
        self.__orm.save_object(new_user)
        current_user = self.__orm.search_objects(
            Users(), {"identity_card": user["identity_card"]})
        id_user = current_user[0].get_id()

        if self.__orm.search_objects(Users(), {"id": id_user}):
            new_account = Account()
            new_account.load_attributes([0, user["username"],
                                         user["password"],
                                         id_user,
                                         user["id_role"]])
            self.__orm.save_object(new_account)
            return True
        return False

    def get_all_user(self) -> List[Dict[str, Any]]:
        """This method returns all the users that are in the database,
        If there are users, return a list of users.
        otherwise it returns false."""
        object_list = self.__orm.get_objects_from_the_table(Users())
        if object_list:
            users_list = []
            for user in object_list:
                users_list.append(user.__dict__)
            return users_list
        return []

    def get_user(self, identifier: str) -> Dict[str, Any]:
        """This method searches for a user in the database,
        If found, return all user data,
        otherwise, returns a dic false."""
        user = self.__orm.search_objects(
            Users(), {"id": identifier})
        if user:
            return user[0].__dict__
        return {}

    def delete_user(self, identifier: str) -> Union[Any, bool]:
        """This method searches for a user in the database,
        If found, return all user data,
        otherwise, returns a false."""
        user = self.get_user(identifier)
        if user:
            user_to_delete = Users()
            user_to_delete.load_attributes([user['_id'],
                                            user["_first_name"],
                                            user["_last_name"],
                                            user["_identity_card"],
                                            user["_phone"],
                                            user["_email"],
                                            user["_birthday"]])
            action = self.__orm.object_delete(user_to_delete)
            return action
        return False
