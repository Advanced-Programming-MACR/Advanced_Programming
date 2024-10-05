"""
This module contains a class that will be the products of the shop.

Author: Miguel Andres Contreras Rodriguez <macontrerasr@udistrital.edu.co>

This file is part of Workshop2.

Workshop2 is free software: you can redistribute it and/or 
modify it under the terms of the GNU General Public License as 
published by the Free Software Foundation, either version 3 of 
the License, or (at your option) any later version.

Workshop2 is distributed in the hope that it will be useful, 
but WITHOUT ANY WARRANTY; without even the implied warranty of 
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU 
General Public License for more details.

You should have received a copy of the GNU General Public License 
along with Workshop2. If not, see <https://www.gnu.org/licenses/>. 
"""


class Product:
    """
    Represents a product with various attributes such as name, ID, description, brand,
    price, and quantity.

    Attributes:
        __name (str): The name of the product.
        __id (int): The unique identifier for the product.
        __description (str): A brief description of the product.
        __brand (str): The brand of the product.
        __price (float): The price of the product.
        __quantity (int): The quantity of the product in stock.

    Methods:

        is_name: Checks if the given name is part of the product's name (case-insensitive).
        is_id: Checks if the given ID matches the product's ID.
        is_brand: Checks if the given brand is part of the product's brand (case-insensitive).
        change_stock: Adjusts the product's stock quantity by the specified number.
        is_no_stock: Checks if the product is out of stock.
    """

    def __init__(
        self,
        name: str,
        id_: int,
        description: str,
        brand: str,
        price: float,
        quantity: int,
    ):
        self.__name = name
        self.__id = id_
        self.__description = description
        self.__brand = brand
        self.__price = price
        self.__quantity = quantity

    def __str__(self) -> str:
        return f"{self.__name}: ${self.__price}\n{self.__description}\
        \nBrand: {self.__brand}\nStock: {'No stock' if self.__quantity == 0 else ''}\
        \nid: {self.__id}"

    def is_name(self, name: str) -> bool:
        """
        Checks if the given name is part of the product's name (case-insensitive).

        Args:
            name (str): The name to check.

        Returns:
            bool: True if the name is part of the product's name, False otherwise.
        """
        return True if name in self.__name.lower() else False

    def is_id(self, id_: int) -> bool:
        """
        Checks if the given ID matches the product's ID.

        Args:
            id_ (int): The ID to check.

        Returns:
            bool: True if the ID matches the product's ID, False otherwise.
        """
        return True if id_ == self.__id else False

    def is_brand(self, brand: str) -> bool:
        """
        Checks if the given brand is part of the product's brand (case-insensitive).

        Args:
            brand (str): The brand to check.

        Returns:
            bool: True if the brand is part of the product's brand, False otherwise.
        """
        return True if brand in self.__brand.lower() else False

    def change_stock(self, num: int):
        """
        Adjusts the product's stock quantity by adding a number,

        Args:
            num (int): The number to adjust the stock by.
        """
        self.__quantity = self.__quantity + num

    def is_no_stock(self) -> bool:
        """
        Checks if the product is out of stock.

        Returns:
            bool: True if the product is out of stock, False otherwise.
        """
        return True if self.__quantity == 0 else False
