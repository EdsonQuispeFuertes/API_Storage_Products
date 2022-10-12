"""This module contains the product base object."""
from typing import List, Any

from source_orm.orm_base_object import OrmBaseObject


class Product(OrmBaseObject):
    """This class is the product's model object."""

    def __init__(self) -> None:
        OrmBaseObject.__init__(self)
        self._name: str = ""
        self._long_description: str = ""
        self._short_description: str = ""
        self._dimensions: str = ""
        self._weight: str = ""
        self._image_one: str = ""
        self._image_two: str = ""
        self._image_three: str = ""
        self._image_four: str = ""
        self._quantity: int = 0
        self._price: float = 0

    def id_product(self) -> Any:
        """This method returns the id product."""
        return self._id

    def name(self) -> str:
        """This method returns the name."""
        return self._name

    def long_description(self) -> str:
        """This method returns the long description."""
        return self._long_description

    def short_description(self) -> str:
        """This method returns the short description."""
        return self._short_description

    def dimensions(self) -> str:
        """This method returns the dimensions."""
        return self._dimensions

    def weight(self) -> str:
        """This method returns the weight."""
        return self._weight

    def images(self) -> List[str]:
        """This method returns the image."""
        return [self._image_one, self._image_two,
                self._image_three, self._image_four]

    def quantity(self) -> int:
        """This method returns the quantity."""
        return self._quantity

    def price(self) -> float:
        """This method returns the price."""
        return self._price

    def load_attributes(self, list_arguments: List[Any]) -> None:
        """This method loads its value to the attributes,
        using an order with the indexes of a list.
        That list is received as a parameter."""
        if isinstance(list_arguments, list):
            self._id = list_arguments[0]
            self._name = list_arguments[1]
            self._long_description = list_arguments[2]
            self._short_description = list_arguments[3]
            self._dimensions = list_arguments[4]
            self._weight = list_arguments[5]
            self._image_one = list_arguments[6]
            self._image_two = list_arguments[7]
            self._image_three = list_arguments[8]
            self._image_four = list_arguments[9]
            self._quantity = list_arguments[10]
            self._price = list_arguments[11]
        elif isinstance(list_arguments, dict):
            self._id = list_arguments.get("id")
            self._name = list_arguments["name"]
            self._long_description = list_arguments["long_description"]
            self._short_description = list_arguments["short_description"]
            self._dimensions = list_arguments["dimensions"]
            self._weight = list_arguments["weight"]
            self._image_one = list_arguments["image_one"]
            self._image_two = list_arguments["image_two"]
            self._image_three = list_arguments["image_three"]
            self._image_four = list_arguments["image_four"]
            self._quantity = list_arguments["quantity"]
            self._price = list_arguments["price"]
