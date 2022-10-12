"""This module contains the orm product class."""
from typing import Dict, Union, Any

from orm import Orm

from model.product import Product


class OrmProduct:
    """This class is the orm product."""

    def __init__(self, orm: Orm):
        self.__orm = orm

    def get_product(self, identifier: str) -> Union[Any, bool]:
        """This method searches for a product in the database,
        If found, return all product data,
        otherwise, returns a false."""
        product = self.__orm.search_objects(
            Product(), {"id": identifier})
        if product:
            return product[0].__dict__
        return False

    def get_products(self) -> Union[Any, bool]:
        """This method returns all the products that are in the database,
        If there are products, return a list of products.
        otherwise it returns false."""
        object_list = self.__orm.get_objects_from_the_table(Product())
        if object_list:
            list_products = []
            for product in object_list:
                list_products.append(product.__dict__)
            return list_products
        return False

    def create_product(self, product: Dict[str, str]) -> bool:
        """This method creates a new product.
        First it is verified if the product is already registered,
        If the product already exists, it returns false.
        If the product does not exist,
        a new product is created with the dictionary entered.
        Then it returns true."""
        if self.__orm.search_objects(
                Product(), {"name": product["name"]}):
            return False
        new_product = Product()
        new_product.load_attributes([0,
                                     product["name"],
                                     product["long_description"],
                                     product["short_description"],
                                     product["dimensions"],
                                     product["weight"],
                                     product["image_one"],
                                     product["image_two"],
                                     product["image_three"],
                                     product["image_four"],
                                     product["quantity"],
                                     product["price"]])
        self.__orm.save_object(new_product)
        return True
